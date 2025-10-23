from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from datetime import datetime
import uuid

# User Models
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    phone: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: EmailStr
    password: str
    phone: Optional[str] = None
    address: Optional[str] = None
    createdAt: datetime = Field(default_factory=datetime.utcnow)

# Product Models
class Product(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    category: str
    categoryId: str
    price: float
    originalPrice: Optional[float] = None
    image: str
    description: str
    weight: Optional[str] = None
    inStock: bool = True
    rating: Optional[float] = None
    reviews: Optional[int] = None

# Order Models
class OrderItem(BaseModel):
    productId: str
    name: str
    quantity: int
    price: float
    image: Optional[str] = None

class ShippingAddress(BaseModel):
    name: str
    email: Optional[str] = None
    phone: str
    address: str
    city: str
    state: str
    pincode: str
    notes: Optional[str] = None

class OrderCreate(BaseModel):
    amount: int  # in paise
    items: List[OrderItem]
    shippingAddress: ShippingAddress

class PaymentVerification(BaseModel):
    orderId: str
    razorpayPaymentId: str
    razorpayOrderId: str
    razorpaySignature: str

class Order(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    orderId: str
    userId: Optional[str] = None
    items: List[OrderItem]
    totalAmount: float
    shippingAddress: ShippingAddress
    razorpayOrderId: str
    razorpayPaymentId: Optional[str] = None
    status: str = 'pending'  # pending, processing, delivered, cancelled
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    updatedAt: datetime = Field(default_factory=datetime.utcnow)

# Category Model
class Category(BaseModel):
    id: str
    name: str
    image: str
    description: str
