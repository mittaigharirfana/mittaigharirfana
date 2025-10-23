import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os

# Database connection
mongo_url = os.environ.get('MONGO_URL', 'mongodb://localhost:27017')
client = AsyncIOMotorClient(mongo_url)
db = client['freshwala_db']

# Category images from freshwala.online
category_images = {
    'Podulu (Spice Powders)': 'https://www.freshwala.online/images/category-podulu.jpg',
    'Dehydrated Powders': 'https://www.freshwala.online/images/category-dehydrated.jpg',
    'Dairy Products': 'https://www.freshwala.online/images/category-dairy.jpg',
    'Papad': 'https://www.freshwala.online/images/category-papad.jpg',
    'Pickles': 'https://www.freshwala.online/images/category-pickles.jpg',
    'Batters': 'https://www.freshwala.online/images/category-batters.jpg'
}

async def update_category_images():
    print("Updating category images...")
    
    for category_name, image_url in category_images.items():
        result = await db.categories.update_one(
            {'name': category_name},
            {'$set': {'image': image_url}}
        )
        
        if result.modified_count > 0:
            print(f"✅ Updated: {category_name}")
        else:
            print(f"⚠️  Not found: {category_name}")
    
    print("\n✅ All category images updated!")
    client.close()

if __name__ == "__main__":
    asyncio.run(update_category_images())
