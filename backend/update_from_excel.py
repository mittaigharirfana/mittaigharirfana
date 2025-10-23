import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
import openpyxl

# Database connection
mongo_url = os.environ.get('MONGO_URL', 'mongodb://localhost:27017')
client = AsyncIOMotorClient(mongo_url)
db = client['freshwala_db']

async def update_images_from_excel():
    # Load the Excel file
    wb = openpyxl.load_workbook('/tmp/freshwala_images.xlsx')
    sheet = wb.active
    
    print("Updating product images from Excel...")
    updated_count = 0
    not_found_count = 0
    
    for row in sheet.iter_rows(min_row=2, values_only=True):
        if row[0] and row[1]:  # Product name and Image URL
            product_name = str(row[0]).strip()
            image_url = str(row[1]).strip()
            
            # Remove "Organic" prefix for matching
            search_name = product_name.replace('Organic ', '')
            
            # Try to find and update the product
            result = await db.products.update_one(
                {'name': {'$regex': search_name, '$options': 'i'}},
                {'$set': {'image': image_url}}
            )
            
            if result.modified_count > 0:
                print(f"✅ Updated: {search_name} -> {image_url}")
                updated_count += 1
            else:
                # Try exact match
                result = await db.products.update_one(
                    {'name': search_name},
                    {'$set': {'image': image_url}}
                )
                if result.modified_count > 0:
                    print(f"✅ Updated: {search_name} -> {image_url}")
                    updated_count += 1
                else:
                    print(f"⚠️  Not found: {search_name}")
                    not_found_count += 1
    
    print(f"\n✅ Updated: {updated_count} products")
    print(f"⚠️  Not found: {not_found_count} products")
    
    client.close()

if __name__ == "__main__":
    asyncio.run(update_images_from_excel())
