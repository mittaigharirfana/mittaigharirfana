import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

async def check_categories():
    client = AsyncIOMotorClient(MONGO_URL)
    db = client.freshwala
    
    print("📊 Checking all categories in database...")
    categories = await db.categories.find().to_list(length=None)
    
    if not categories:
        print("⚠️  No categories found in database!")
    else:
        print(f"\n✅ Found {len(categories)} categories:")
        for i, cat in enumerate(categories, 1):
            print(f"\n{i}. Category ID: {cat.get('id')}")
            print(f"   Name: {cat.get('name')}")
            print(f"   Image: {cat.get('image', 'NO IMAGE')}")
    
    client.close()

if __name__ == "__main__":
    asyncio.run(check_categories())
