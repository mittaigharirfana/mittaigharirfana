import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
from seed_data import categories_data

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

async def reseed_categories():
    client = AsyncIOMotorClient(MONGO_URL)
    db = client.freshwala_db
    
    print("🗑️  Clearing existing categories...")
    delete_result = await db.categories.delete_many({})
    print(f"   Deleted {delete_result.deleted_count} categories")
    
    print("\n🌱 Seeding new categories with updated images...")
    await db.categories.insert_many(categories_data)
    print(f"   Inserted {len(categories_data)} categories")
    
    print("\n📊 Verification - All categories:")
    categories = await db.categories.find({}, {'_id': 0}).to_list(length=None)
    for cat in categories:
        print(f"\n  ✅ {cat['name']}")
        print(f"     ID: {cat['id']}")
        print(f"     Image: {cat['image'][:60]}...")
        print(f"     Description: {cat['description']}")
    
    client.close()
    print("\n✅ Category reseed complete!")

if __name__ == "__main__":
    asyncio.run(reseed_categories())
