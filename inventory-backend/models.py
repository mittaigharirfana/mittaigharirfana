from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum

class ProductCategory(str, Enum):
    MILK = "Milk"
    CURD = "Curd"
    GHEE = "Ghee"
    PANEER = "Paneer"
    PICKLES = "Pickles"

class UnitType(str, Enum):
    LITERS = "Liters"
    KG = "Kg"
    PIECES = "Pieces"
    GRAMS = "Grams"

# Product Model
class Product(BaseModel):
    id: str = Field(default=None)
    name: str
    category: ProductCategory
    unit: UnitType
    current_stock: float = 0.0
    min_stock_level: float = 0.0
    cost_price: float = 0.0
    selling_price: float = 0.0
    supplier_id: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

# Supplier Model
class Supplier(BaseModel):
    id: str = Field(default=None)
    name: str
    contact_person: str
    phone: str
    email: Optional[str] = None
    address: Optional[str] = None
    products_supplied: List[str] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)

# Purchase Model
class Purchase(BaseModel):
    id: str = Field(default=None)
    product_id: str
    product_name: str
    supplier_id: str
    supplier_name: str
    quantity: float
    unit: UnitType
    cost_price: float
    total_cost: float
    purchase_date: datetime = Field(default_factory=datetime.utcnow)
    notes: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

# Sales Model
class Sale(BaseModel):
    id: str = Field(default=None)
    product_id: str
    product_name: str
    quantity: float
    unit: UnitType
    selling_price: float
    total_amount: float
    cost_price: float
    profit: float
    sale_date: datetime = Field(default_factory=datetime.utcnow)
    customer_name: Optional[str] = None
    notes: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

# Stock Alert Model
class StockAlert(BaseModel):
    id: str = Field(default=None)
    product_id: str
    product_name: str
    current_stock: float
    min_stock_level: float
    alert_date: datetime = Field(default_factory=datetime.utcnow)
    is_resolved: bool = False

# User Model
class User(BaseModel):
    id: str = Field(default=None)
    username: str
    email: str
    password_hash: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

# Create/Update Models
class ProductCreate(BaseModel):
    name: str
    category: ProductCategory
    unit: UnitType
    current_stock: float = 0.0
    min_stock_level: float = 0.0
    cost_price: float = 0.0
    selling_price: float = 0.0
    supplier_id: Optional[str] = None

class SupplierCreate(BaseModel):
    name: str
    contact_person: str
    phone: str
    email: Optional[str] = None
    address: Optional[str] = None
    products_supplied: List[str] = []

class PurchaseCreate(BaseModel):
    product_id: str
    supplier_id: str
    quantity: float
    cost_price: float
    purchase_date: Optional[datetime] = None
    notes: Optional[str] = None

class SaleCreate(BaseModel):
    product_id: str
    quantity: float
    selling_price: Optional[float] = None
    sale_date: Optional[datetime] = None
    customer_name: Optional[str] = None
    notes: Optional[str] = None
