import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os

# Database connection
mongo_url = os.environ.get('MONGO_URL', 'mongodb://localhost:27017')
client = AsyncIOMotorClient(mongo_url)
db = client['freshwala_db']

# Using placeholder images that work
PLACEHOLDER_BASE = "https://via.placeholder.com/400x400/f97316/ffffff?text="

async def fix_images():
    print("Updating all product and category images with working URLs...")
    
    # Get all products
    products = await db.products.find({}).to_list(1000)
    
    for product in products:
        # Create a simple placeholder with product name
        product_name = product['name'].replace(' ', '+')
        placeholder_url = f"{PLACEHOLDER_BASE}{product_name}"
        
        await db.products.update_one(
            {'id': product['id']},
            {'$set': {'image': placeholder_url}}
        )
        print(f"Updated: {product['name']}")
    
    # Get all categories
    categories = await db.categories.find({}).to_list(100)
    
    for category in categories:
        category_name = category['name'].replace(' ', '+')
        placeholder_url = f"{PLACEHOLDER_BASE}{category_name}"
        
        await db.categories.update_one(
            {'id': category['id']},
            {'$set': {'image': placeholder_url}}
        )
        print(f"Updated category: {category['name']}")
    
    print("\nAll images updated successfully!")
    print("\nNOTE: These are placeholder images.")
    print("To add your real product images:")
    print("1. Upload your product images to a public hosting service (Imgur, Google Drive, etc.)")
    print("2. Use the admin panel at www.freshwala.online/admin/login to update each product")
    print("3. Or provide me with publicly accessible image URLs and I'll update them")
    
    client.close()

if __name__ == "__main__":
    asyncio.run(fix_images())
