import os
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime

# MongoDB connection
MONGO_URL = os.environ.get('MONGO_URL', 'mongodb://localhost:27017')
client = AsyncIOMotorClient(MONGO_URL)
db = client['freshwala_inventory']

# Collections
products_collection = db['products']
purchases_collection = db['purchases']
sales_collection = db['sales']
suppliers_collection = db['suppliers']
alerts_collection = db['alerts']
users_collection = db['users']
