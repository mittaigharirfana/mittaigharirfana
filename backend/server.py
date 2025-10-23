from fastapi import FastAPI, APIRouter, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pathlib import Path
import os
import logging
import razorpay
import hmac
import hashlib
from datetime import datetime
import uuid

from models import (
    OrderCreate, PaymentVerification, Order, OrderItem,
    Product, Category, UserLogin
)
from database import (
    products_collection, orders_collection, categories_collection,
    close_db
)
from seed_data import products_data, categories_data

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# Razorpay client
razorpay_client = razorpay.Client(
    auth=(os.environ['RAZORPAY_KEY_ID'], os.environ['RAZORPAY_KEY_SECRET'])
)

# Create the main app
app = FastAPI()

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Seed database on startup
@app.on_event("startup")
async def startup_event():
    # Seed categories
    existing_categories = await categories_collection.count_documents({})
    if existing_categories == 0:
        await categories_collection.insert_many(categories_data)
        logger.info("Seeded categories")
    
    # Seed products
    existing_products = await products_collection.count_documents({})
    if existing_products == 0:
        await products_collection.insert_many(products_data)
        logger.info("Seeded products")

@app.on_event("shutdown")
async def shutdown_event():
    await close_db()

# Basic route
@api_router.get("/")
async def root():
    return {"message": "Freshwala API is running"}

# Get all categories
@api_router.get("/categories")
async def get_categories():
    categories = await categories_collection.find({}, {'_id': 0}).to_list(100)
    return categories

# Get all products with optional filters
@api_router.get("/products")
async def get_products(
    category: str = None,
    search: str = None,
    minPrice: float = None,
    maxPrice: float = None
):
    query = {}
    
    if category:
        query['category'] = category
    
    if search:
        query['$or'] = [
            {'name': {'$regex': search, '$options': 'i'}},
            {'description': {'$regex': search, '$options': 'i'}}
        ]
    
    if minPrice is not None or maxPrice is not None:
        query['price'] = {}
        if minPrice is not None:
            query['price']['$gte'] = minPrice
        if maxPrice is not None:
            query['price']['$lte'] = maxPrice
    
    products = await products_collection.find(query, {'_id': 0}).to_list(1000)
    return products

# Get single product
@api_router.get("/products/{product_id}")
async def get_product(product_id: str):
    product = await products_collection.find_one({'id': product_id}, {'_id': 0})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Create order and Razorpay order
@api_router.post("/orders/create")
async def create_order(order_data: OrderCreate):
    try:
        # Create Razorpay order
        razorpay_order = razorpay_client.order.create({
            'amount': order_data.amount,
            'currency': 'INR',
            'payment_capture': 1
        })
        
        # Generate unique order ID
        order_id = f"ORD{uuid.uuid4().hex[:8].upper()}"
        
        # Create order in database
        order = Order(
            orderId=order_id,
            items=order_data.items,
            totalAmount=order_data.amount / 100,  # Convert paise to rupees
            shippingAddress=order_data.shippingAddress,
            razorpayOrderId=razorpay_order['id'],
            status='pending'
        )
        
        order_dict = order.dict()
        await orders_collection.insert_one(order_dict)
        
        logger.info(f"Order created: {order_id}, Razorpay Order: {razorpay_order['id']}")
        
        return {
            'orderId': order_id,
            'razorpayOrderId': razorpay_order['id']
        }
    except Exception as e:
        logger.error(f"Error creating order: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# Verify payment
@api_router.post("/orders/verify-payment")
async def verify_payment(payment_data: PaymentVerification):
    try:
        # Verify signature
        generated_signature = hmac.new(
            os.environ['RAZORPAY_KEY_SECRET'].encode(),
            f"{payment_data.razorpayOrderId}|{payment_data.razorpayPaymentId}".encode(),
            hashlib.sha256
        ).hexdigest()
        
        if generated_signature != payment_data.razorpaySignature:
            raise HTTPException(status_code=400, detail="Invalid payment signature")
        
        # Update order status
        result = await orders_collection.update_one(
            {'orderId': payment_data.orderId},
            {
                '$set': {
                    'razorpayPaymentId': payment_data.razorpayPaymentId,
                    'status': 'processing',
                    'updatedAt': datetime.utcnow()
                }
            }
        )
        
        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail="Order not found")
        
        logger.info(f"Payment verified for order: {payment_data.orderId}")
        
        return {'success': True, 'message': 'Payment verified successfully'}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error verifying payment: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# Get all orders
@api_router.get("/orders")
async def get_orders():
    orders = await orders_collection.find({}, {'_id': 0}).sort('createdAt', -1).to_list(1000)
    return orders

# Get specific order
@api_router.get("/orders/{order_id}")
async def get_order(order_id: str):
    order = await orders_collection.find_one({'orderId': order_id}, {'_id': 0})
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

# Include the router in the main app
app.include_router(api_router)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
