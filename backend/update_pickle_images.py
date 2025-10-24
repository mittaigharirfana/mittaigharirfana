import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
DB_NAME = os.getenv("DB_NAME")

# Mapping of pickle products to images
PICKLE_IMAGES = {
    "lemon pickle": "https://images.unsplash.com/photo-1617854307432-13950e24ba07",
    "tomato pickle": "https://images.unsplash.com/photo-1601702538934-efffab67ab65",
    "tamarind pickle": "https://images.unsplash.com/photo-1627861446476-42fd9925e151",
    "amla pickle": "https://images.unsplash.com/photo-1651959653830-5c8cb576e134",
    "drumstick pickle": "https://images.unsplash.com/photo-1664791461482-79f5deee490f",
    "chicken pickle": "https://images.unsplash.com/photo-1659694459412-02735752031f",
    "brinjal pickle": "https://images.pexels.com/photos/12392833/pexels-photo-12392833.jpeg",
    "mutton pickle": "https://images.unsplash.com/photo-1757802261964-a8e03ed98981"
}

async def update_pickle_images():
    client = AsyncIOMotorClient(MONGO_URL)
    db = client[DB_NAME]
    
    print("🔍 Searching for pickle products...")
    
    # Find all products
    all_products = await db.products.find({}, {'_id': 0}).to_list(length=None)
    
    updated_count = 0
    not_found = []
    
    for pickle_name, image_url in PICKLE_IMAGES.items():
        # Search for product by name (case insensitive)
        product = await db.products.find_one(
            {"name": {"$regex": pickle_name, "$options": "i"}}
        )
        
        if product:
            result = await db.products.update_one(
                {"id": product["id"]},
                {"$set": {"image": image_url}}
            )
            if result.modified_count > 0:
                print(f"✅ Updated: {product['name']} -> {image_url[:60]}...")
                updated_count += 1
            else:
                print(f"ℹ️  {product['name']} already has this image")
        else:
            not_found.append(pickle_name)
            print(f"⚠️  Not found: {pickle_name}")
    
    print(f"\n📊 Summary:")
    print(f"   Updated: {updated_count} products")
    print(f"   Not found: {len(not_found)} products")
    
    if not_found:
        print(f"\n❌ Products not found in database:")
        for name in not_found:
            print(f"   - {name}")
    
    client.close()
    print("\n✅ Update complete!")

if __name__ == "__main__":
    asyncio.run(update_pickle_images())
