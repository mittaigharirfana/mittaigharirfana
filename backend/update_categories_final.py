import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

# Category name mapping to image URLs
CATEGORY_IMAGES = {
    "Pickles": "https://images.unsplash.com/photo-1617854307432-13950e24ba07",
    "Papad": "https://images.pexels.com/photos/8818667/pexels-photo-8818667.jpeg",
    "Batters": "https://images.unsplash.com/photo-1589301760014-d929f3979dbc",
    "Podulu": "https://images.unsplash.com/photo-1698557048177-a460bb415177",
    "Dairy products": "https://images.unsplash.com/photo-1635436338433-89747d0ca0ef"
}

async def update_category_images():
    client = AsyncIOMotorClient(MONGO_URL)
    db = client.freshwala
    
    print("🔄 Starting category image update...")
    
    for category_name, image_url in CATEGORY_IMAGES.items():
        result = await db.categories.update_one(
            {"name": category_name},
            {"$set": {"image": image_url}}
        )
        
        if result.matched_count > 0:
            print(f"✅ Updated {category_name}: {image_url}")
        else:
            print(f"⚠️  Category '{category_name}' not found in database")
    
    # Verify updates
    print("\n📊 Verification - Current category images:")
    categories = await db.categories.find().to_list(length=None)
    for cat in categories:
        print(f"  - {cat['name']}: {cat.get('image', 'NO IMAGE')}")
    
    client.close()
    print("\n✅ Category image update complete!")

if __name__ == "__main__":
    asyncio.run(update_category_images())
