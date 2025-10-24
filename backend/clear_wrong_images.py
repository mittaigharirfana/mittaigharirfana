import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
DB_NAME = os.getenv("DB_NAME")

# Products to clear images
PRODUCTS_TO_CLEAR = [
    "tomato pickle",
    "drumstick pickle",
    "amla pickle",
    "brinjal pickle",
    "mutton pickle"
]

# Placeholder image URL
PLACEHOLDER_IMAGE = "https://images.unsplash.com/photo-1617854307432-13950e24ba07"

async def clear_images():
    client = AsyncIOMotorClient(MONGO_URL)
    db = client[DB_NAME]
    
    print("🔄 Clearing incorrect pickle images...\n")
    
    for product_name in PRODUCTS_TO_CLEAR:
        # Search for product by name (case insensitive)
        product = await db.products.find_one(
            {"name": {"$regex": product_name, "$options": "i"}}
        )
        
        if product:
            result = await db.products.update_one(
                {"id": product["id"]},
                {"$set": {"image": PLACEHOLDER_IMAGE}}
            )
            if result.modified_count > 0:
                print(f"✅ Cleared image: {product['name']}")
                print(f"   Set to placeholder for you to update via admin panel\n")
        else:
            print(f"⚠️  Not found: {product_name}\n")
    
    print("\n✅ Image clearing complete!")
    print("\n📝 You can now update these images via Admin Panel:")
    print("   1. Go to: https://freshwala.online/admin/login")
    print("   2. Login with your admin credentials")
    print("   3. Navigate to 'Manage Products'")
    print("   4. Click 'Edit' button on each product")
    print("   5. Update the 'Image URL' field with correct image links")
    
    client.close()

if __name__ == "__main__":
    asyncio.run(clear_images())
