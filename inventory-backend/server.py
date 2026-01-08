from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import datetime, timedelta
from typing import List, Optional
import uuid
from passlib.context import CryptContext
from jose import JWTError, jwt
import os

from database import (
    products_collection, purchases_collection, sales_collection,
    suppliers_collection, alerts_collection, users_collection
)
from models import (
    Product, ProductCreate, Purchase, PurchaseCreate, Sale, SaleCreate,
    Supplier, SupplierCreate, StockAlert, User
)

app = FastAPI(title="Freshwala Inventory Management API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security
SECRET_KEY = os.environ.get("SECRET_KEY", "your-secret-key-change-this")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()

# Helper functions
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = credentials.credentials
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

# Check and create low stock alerts
async def check_stock_alerts(product_id: str):
    product = await products_collection.find_one({"id": product_id})
    if product and product['current_stock'] <= product['min_stock_level']:
        # Check if alert already exists
        existing_alert = await alerts_collection.find_one({
            "product_id": product_id,
            "is_resolved": False
        })
        if not existing_alert:
            alert = {
                "id": str(uuid.uuid4()),
                "product_id": product_id,
                "product_name": product['name'],
                "current_stock": product['current_stock'],
                "min_stock_level": product['min_stock_level'],
                "alert_date": datetime.utcnow(),
                "is_resolved": False
            }
            await alerts_collection.insert_one(alert)

# ============ AUTH ENDPOINTS ============

@app.post("/api/auth/register")
async def register(username: str, email: str, password: str):
    # Check if user exists
    existing_user = await users_collection.find_one({"$or": [{"username": username}, {"email": email}]})
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    
    user = {
        "id": str(uuid.uuid4()),
        "username": username,
        "email": email,
        "password_hash": hash_password(password),
        "created_at": datetime.utcnow()
    }
    await users_collection.insert_one(user)
    return {"message": "User created successfully"}

@app.post("/api/auth/login")
async def login(username: str, password: str):
    user = await users_collection.find_one({"username": username})
    if not user or not verify_password(password, user['password_hash']):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": username})
    return {"access_token": access_token, "token_type": "bearer", "username": username}

# ============ PRODUCT ENDPOINTS ============

@app.get("/api/products", response_model=List[Product])
async def get_products(username: str = Depends(get_current_user)):
    products = await products_collection.find().to_list(1000)
    return products

@app.get("/api/products/{product_id}", response_model=Product)
async def get_product(product_id: str, username: str = Depends(get_current_user)):
    product = await products_collection.find_one({"id": product_id})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/api/products", response_model=Product)
async def create_product(product: ProductCreate, username: str = Depends(get_current_user)):
    product_dict = product.dict()
    product_dict['id'] = str(uuid.uuid4())
    product_dict['created_at'] = datetime.utcnow()
    product_dict['updated_at'] = datetime.utcnow()
    
    await products_collection.insert_one(product_dict)
    await check_stock_alerts(product_dict['id'])
    return product_dict

@app.put("/api/products/{product_id}", response_model=Product)
async def update_product(product_id: str, product: ProductCreate, username: str = Depends(get_current_user)):
    product_dict = product.dict()
    product_dict['updated_at'] = datetime.utcnow()
    
    result = await products_collection.update_one(
        {"id": product_id},
        {"$set": product_dict}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    
    updated_product = await products_collection.find_one({"id": product_id})
    await check_stock_alerts(product_id)
    return updated_product

@app.delete("/api/products/{product_id}")
async def delete_product(product_id: str, username: str = Depends(get_current_user)):
    result = await products_collection.delete_one({"id": product_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}

# ============ SUPPLIER ENDPOINTS ============

@app.get("/api/suppliers", response_model=List[Supplier])
async def get_suppliers(username: str = Depends(get_current_user)):
    suppliers = await suppliers_collection.find().to_list(1000)
    return suppliers

@app.get("/api/suppliers/{supplier_id}", response_model=Supplier)
async def get_supplier(supplier_id: str, username: str = Depends(get_current_user)):
    supplier = await suppliers_collection.find_one({"id": supplier_id})
    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return supplier

@app.post("/api/suppliers", response_model=Supplier)
async def create_supplier(supplier: SupplierCreate, username: str = Depends(get_current_user)):
    supplier_dict = supplier.dict()
    supplier_dict['id'] = str(uuid.uuid4())
    supplier_dict['created_at'] = datetime.utcnow()
    
    await suppliers_collection.insert_one(supplier_dict)
    return supplier_dict

@app.put("/api/suppliers/{supplier_id}", response_model=Supplier)
async def update_supplier(supplier_id: str, supplier: SupplierCreate, username: str = Depends(get_current_user)):
    result = await suppliers_collection.update_one(
        {"id": supplier_id},
        {"$set": supplier.dict()}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Supplier not found")
    
    updated_supplier = await suppliers_collection.find_one({"id": supplier_id})
    return updated_supplier

@app.delete("/api/suppliers/{supplier_id}")
async def delete_supplier(supplier_id: str, username: str = Depends(get_current_user)):
    result = await suppliers_collection.delete_one({"id": supplier_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return {"message": "Supplier deleted successfully"}

# ============ PURCHASE ENDPOINTS ============

@app.get("/api/purchases", response_model=List[Purchase])
async def get_purchases(username: str = Depends(get_current_user)):
    purchases = await purchases_collection.find().sort("purchase_date", -1).to_list(1000)
    return purchases

@app.get("/api/purchases/{purchase_id}", response_model=Purchase)
async def get_purchase(purchase_id: str, username: str = Depends(get_current_user)):
    purchase = await purchases_collection.find_one({"id": purchase_id})
    if not purchase:
        raise HTTPException(status_code=404, detail="Purchase not found")
    return purchase

@app.post("/api/purchases", response_model=Purchase)
async def create_purchase(purchase: PurchaseCreate, username: str = Depends(get_current_user)):
    # Get product and supplier details
    product = await products_collection.find_one({"id": purchase.product_id})
    supplier = await suppliers_collection.find_one({"id": purchase.supplier_id})
    
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    
    # Create purchase record
    purchase_dict = purchase.dict()
    purchase_dict['id'] = str(uuid.uuid4())
    purchase_dict['product_name'] = product['name']
    purchase_dict['supplier_name'] = supplier['name']
    purchase_dict['unit'] = product['unit']
    purchase_dict['total_cost'] = purchase.quantity * purchase.cost_price
    purchase_dict['created_at'] = datetime.utcnow()
    if not purchase_dict.get('purchase_date'):
        purchase_dict['purchase_date'] = datetime.utcnow()
    
    await purchases_collection.insert_one(purchase_dict)
    
    # Update product stock
    new_stock = product['current_stock'] + purchase.quantity
    await products_collection.update_one(
        {"id": purchase.product_id},
        {"$set": {"current_stock": new_stock, "cost_price": purchase.cost_price}}
    )
    
    # Check if alert should be resolved
    if new_stock > product['min_stock_level']:
        await alerts_collection.update_many(
            {"product_id": purchase.product_id, "is_resolved": False},
            {"$set": {"is_resolved": True}}
        )
    
    return purchase_dict

# ============ SALES ENDPOINTS ============

@app.get("/api/sales", response_model=List[Sale])
async def get_sales(username: str = Depends(get_current_user)):
    sales = await sales_collection.find().sort("sale_date", -1).to_list(1000)
    return sales

@app.get("/api/sales/{sale_id}", response_model=Sale)
async def get_sale(sale_id: str, username: str = Depends(get_current_user)):
    sale = await sales_collection.find_one({"id": sale_id})
    if not sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    return sale

@app.post("/api/sales", response_model=Sale)
async def create_sale(sale: SaleCreate, username: str = Depends(get_current_user)):
    # Get product details
    product = await products_collection.find_one({"id": sale.product_id})
    
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    if product['current_stock'] < sale.quantity:
        raise HTTPException(status_code=400, detail="Insufficient stock")
    
    # Create sale record
    selling_price = sale.selling_price if sale.selling_price else product['selling_price']
    total_amount = sale.quantity * selling_price
    cost_price = product['cost_price']
    profit = total_amount - (sale.quantity * cost_price)
    
    sale_dict = sale.dict()
    sale_dict['id'] = str(uuid.uuid4())
    sale_dict['product_name'] = product['name']
    sale_dict['unit'] = product['unit']
    sale_dict['selling_price'] = selling_price
    sale_dict['total_amount'] = total_amount
    sale_dict['cost_price'] = cost_price
    sale_dict['profit'] = profit
    sale_dict['created_at'] = datetime.utcnow()
    if not sale_dict.get('sale_date'):
        sale_dict['sale_date'] = datetime.utcnow()
    
    await sales_collection.insert_one(sale_dict)
    
    # Update product stock
    new_stock = product['current_stock'] - sale.quantity
    await products_collection.update_one(
        {"id": sale.product_id},
        {"$set": {"current_stock": new_stock}}
    )
    
    await check_stock_alerts(sale.product_id)
    
    return sale_dict

# ============ ALERTS ENDPOINTS ============

@app.get("/api/alerts", response_model=List[StockAlert])
async def get_alerts(resolved: Optional[bool] = None, username: str = Depends(get_current_user)):
    query = {}
    if resolved is not None:
        query['is_resolved'] = resolved
    
    alerts = await alerts_collection.find(query).sort("alert_date", -1).to_list(1000)
    return alerts

@app.put("/api/alerts/{alert_id}/resolve")
async def resolve_alert(alert_id: str, username: str = Depends(get_current_user)):
    result = await alerts_collection.update_one(
        {"id": alert_id},
        {"$set": {"is_resolved": True}}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Alert not found")
    return {"message": "Alert resolved"}

# ============ REPORTS ENDPOINTS ============

@app.get("/api/reports/dashboard")
async def get_dashboard_stats(username: str = Depends(get_current_user)):
    # Total products
    total_products = await products_collection.count_documents({})
    
    # Low stock products
    low_stock = await products_collection.count_documents({
        "$expr": {"$lte": ["$current_stock", "$min_stock_level"]}
    })
    
    # Today's sales
    today_start = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    today_sales = await sales_collection.find({"sale_date": {"$gte": today_start}}).to_list(1000)
    today_revenue = sum([sale['total_amount'] for sale in today_sales])
    today_profit = sum([sale['profit'] for sale in today_sales])
    
    # Active alerts
    active_alerts = await alerts_collection.count_documents({"is_resolved": False})
    
    return {
        "total_products": total_products,
        "low_stock_products": low_stock,
        "today_revenue": today_revenue,
        "today_profit": today_profit,
        "active_alerts": active_alerts,
        "today_sales_count": len(today_sales)
    }

@app.get("/api/reports/sales")
async def get_sales_report(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    username: str = Depends(get_current_user)
):
    query = {}
    if start_date:
        query['sale_date'] = {"$gte": datetime.fromisoformat(start_date)}
    if end_date:
        if 'sale_date' in query:
            query['sale_date']['$lte'] = datetime.fromisoformat(end_date)
        else:
            query['sale_date'] = {"$lte": datetime.fromisoformat(end_date)}
    
    sales = await sales_collection.find(query).to_list(1000)
    
    total_revenue = sum([sale['total_amount'] for sale in sales])
    total_profit = sum([sale['profit'] for sale in sales])
    total_sales = len(sales)
    
    # Group by product
    product_sales = {}
    for sale in sales:
        product_name = sale['product_name']
        if product_name not in product_sales:
            product_sales[product_name] = {
                "quantity": 0,
                "revenue": 0,
                "profit": 0
            }
        product_sales[product_name]['quantity'] += sale['quantity']
        product_sales[product_name]['revenue'] += sale['total_amount']
        product_sales[product_name]['profit'] += sale['profit']
    
    return {
        "total_revenue": total_revenue,
        "total_profit": total_profit,
        "total_sales": total_sales,
        "product_breakdown": product_sales,
        "sales": sales
    }

@app.get("/api/reports/purchases")
async def get_purchases_report(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    username: str = Depends(get_current_user)
):
    query = {}
    if start_date:
        query['purchase_date'] = {"$gte": datetime.fromisoformat(start_date)}
    if end_date:
        if 'purchase_date' in query:
            query['purchase_date']['$lte'] = datetime.fromisoformat(end_date)
        else:
            query['purchase_date'] = {"$lte": datetime.fromisoformat(end_date)}
    
    purchases = await purchases_collection.find(query).to_list(1000)
    
    total_cost = sum([purchase['total_cost'] for purchase in purchases])
    total_purchases = len(purchases)
    
    # Group by supplier
    supplier_purchases = {}
    for purchase in purchases:
        supplier_name = purchase['supplier_name']
        if supplier_name not in supplier_purchases:
            supplier_purchases[supplier_name] = {
                "quantity": 0,
                "total_cost": 0
            }
        supplier_purchases[supplier_name]['quantity'] += purchase['quantity']
        supplier_purchases[supplier_name]['total_cost'] += purchase['total_cost']
    
    return {
        "total_cost": total_cost,
        "total_purchases": total_purchases,
        "supplier_breakdown": supplier_purchases,
        "purchases": purchases
    }

@app.get("/api/reports/stock-value")
async def get_stock_value_report(username: str = Depends(get_current_user)):
    products = await products_collection.find().to_list(1000)
    
    total_stock_value = 0
    product_values = []
    
    for product in products:
        value = product['current_stock'] * product['cost_price']
        total_stock_value += value
        product_values.append({
            "product_name": product['name'],
            "current_stock": product['current_stock'],
            "cost_price": product['cost_price'],
            "stock_value": value,
            "unit": product['unit']
        })
    
    return {
        "total_stock_value": total_stock_value,
        "products": product_values
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
