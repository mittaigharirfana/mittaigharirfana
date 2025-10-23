import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
import aiohttp
from bs4 import BeautifulSoup

# Database connection
mongo_url = os.environ.get('MONGO_URL', 'mongodb://localhost:27017')
client = AsyncIOMotorClient(mongo_url)
db = client['freshwala_db']

# Product URLs mapping
product_urls = {
    'Kandi Powder': 'https://www.freshwala.online/product/32721374/Kandi-Powder',
    'Kobbari Powder': 'https://www.freshwala.online/product/32721373/Kobbari-Powder--100Gms',
    'Groundnut Powder': 'https://www.freshwala.online/product/32721372/Groundnut--100Gms',
    'Sesame Powder': 'https://www.freshwala.online/product/32721371/Sessame-100Gms',
    'Coriander Powder': 'https://www.freshwala.online/product/32721370/Coriander--100Gms',
    'Curry Leaves Powder': 'https://www.freshwala.online/product/32721369/Curry-Leaves--100Gms',
    'Carrot Powder': 'https://www.freshwala.online/product/32721368/Chikpeace-Powder--100Gms',
    'Beetroot Powder': 'https://www.freshwala.online/product/32721381/Carrot--100Gms',
    'Moringa Powder': 'https://www.freshwala.online/product/32721379/Moringa-Powder--100Gms',
    'Onion Powder': 'https://www.freshwala.online/product/32721378/Onion-Powder--100Gms',
    'Tomato Powder': 'https://www.freshwala.online/product/32721377/Tomato-100Gms',
    'Ginger Powder': 'https://www.freshwala.online/product/32721376/Ginger--100Gms',
    'Green Chilli Powder': 'https://www.freshwala.online/product/32721375/Green-Chilli--100Gms',
    'Pure Buffalo Ghee': 'https://www.freshwala.online/product/32721386/Pure-Buffalo-Ghee--250Gms',
    'Fresh Butter': 'https://www.freshwala.online/product/32721385/Butter--250Gms',
    'Fresh Paneer': 'https://www.freshwala.online/product/32721384/Paneer--250Gms',
    'Fresh Malai': 'https://www.freshwala.online/product/32721383/Malai--250Gms',
    'Khova': 'https://www.freshwala.online/product/32721382/Khova--250Gms',
    'Home Made Papad': 'https://www.freshwala.online/product/32721393/Home-Made-Papad-250Gms',
    'Masala Papad': 'https://www.freshwala.online/product/32721392/Masala-Papad---250Gms',
    'Urad Dal Papad': 'https://www.freshwala.online/product/32721391/Urad-Dal-Papad---250Gms',
    'Moong Dal Papad': 'https://www.freshwala.online/product/32721390/Moongdal-Papad--250Gms',
    'Tomato Papad': 'https://www.freshwala.online/product/32721389/Tomato-Papad--250Gms',
    'Sabudana Papad': 'https://www.freshwala.online/product/32721388/Sabudana-Papad---250Gms',
    'Green Chilli Papad': 'https://www.freshwala.online/product/32721387/Green-Chilli--250Gms',
    'Mango Pickle': 'https://www.freshwala.online/product/32721412/Mango-Pickle--Freshwala-Mango-Pickle-Mango-Pickle',
    'Lemon Pickle': 'https://www.freshwala.online/product/32721411/Lemon-Pickle',
    'Amla Pickle': 'https://www.freshwala.online/product/32721410/Amla-Pickle',
    'Tamarind Pickle': 'https://www.freshwala.online/product/32721409/Tamrind--250-Gms',
    'Tomato Pickle': 'https://www.freshwala.online/product/32721408/Tomato--250-Gms',
    'Gongura Pickle': 'https://www.freshwala.online/product/32721407/Gongura--250-Gms',
    'Drumstick Pickle': 'https://www.freshwala.online/product/32721405/Drumstick-250-Gms',
    'Pudina Pickle': 'https://www.freshwala.online/product/32721404/Pudina--250-Gms',
    'Ginger Pickle': 'https://www.freshwala.online/product/32721403/Ginger--250-Gms',
    'Garlic Pickle': 'https://www.freshwala.online/product/32721402/Garlic--250-Gms',
    'Coriander Pickle': 'https://www.freshwala.online/product/32721401/Coriander--250-Gms',
    'Curry Leaves Pickle': 'https://www.freshwala.online/product/32721400/Curryleaves--250-Gms',
    'Brinjal Pickle': 'https://www.freshwala.online/product/32721399/Brinjal--250-Gms',
    'Chicken Pickle': 'https://www.freshwala.online/product/32721398/Chicken--250-Gms',
    'Mutton Pickle': 'https://www.freshwala.online/product/32721397/Mutton--250-Gms',
    'Fish Pickle': 'https://www.freshwala.online/product/32721396/Fish--250-Gms',
    'Prawns Pickle': 'https://www.freshwala.online/product/32721395/Prawns--250-Gms',
    'Beef Pickle': 'https://www.freshwala.online/product/32721394/Beef--250-Gms',
    'Idli Batter': 'https://www.freshwala.online/product/32721417/Idli-Batter-Freshwala-Idli-Batter-%25',
    'Dosa Batter': 'https://www.freshwala.online/product/32721416/Dosa-Batter-Home-Made-Fresh-Dosa',
    'Millet Batter': 'https://www.freshwala.online/product/32721415/Millet-Batter-Freshwala-Millet-Batter',
    'Gare Batter': 'https://www.freshwala.online/product/32721414/Gare-Batter',
    'Pesarattu Batter': 'https://www.freshwala.online/product/32721413/Pesarattu'
}

async def fetch_image_from_page(url):
    """Fetch the main product image from the product page"""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
                if response.status == 200:
                    html = await response.text()
                    soup = BeautifulSoup(html, 'html.parser')
                    
                    # Try to find the main product image
                    # Common selectors for product images
                    img = None
                    
                    # Try OpenGraph image
                    og_image = soup.find('meta', property='og:image')
                    if og_image and og_image.get('content'):
                        img = og_image.get('content')
                    
                    # Try schema.org image
                    if not img:
                        schema_img = soup.find('meta', {'itemprop': 'image'})
                        if schema_img and schema_img.get('content'):
                            img = schema_img.get('content')
                    
                    # Try main product image container
                    if not img:
                        main_img = soup.select_one('.product-image img, .main-image img, img[alt*="product"], img[alt*="Product"]')
                        if main_img and main_img.get('src'):
                            img = main_img.get('src')
                    
                    if img and not img.startswith('http'):
                        img = 'https://www.freshwala.online' + img
                    
                    return img
    except Exception as e:
        print(f"Error fetching {url}: {e}")
    return None

async def update_all_images():
    print("Fetching images from product pages...")
    
    for product_name, url in product_urls.items():
        print(f"Processing: {product_name}...")
        
        # Fetch image URL
        image_url = await fetch_image_from_page(url)
        
        if image_url:
            # Find and update product by name
            result = await db.products.update_one(
                {'name': {'$regex': product_name, '$options': 'i'}},
                {'$set': {'image': image_url}}
            )
            if result.modified_count > 0:
                print(f"✅ Updated {product_name}: {image_url}")
            else:
                print(f"⚠️  No match found for {product_name}")
        else:
            print(f"❌ Failed to get image for {product_name}")
        
        await asyncio.sleep(0.5)  # Small delay between requests
    
    print("\n✅ All images updated!")
    client.close()

if __name__ == "__main__":
    asyncio.run(update_all_images())
