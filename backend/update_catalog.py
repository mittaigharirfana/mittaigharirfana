import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os

# Database connection
mongo_url = os.environ.get('MONGO_URL', 'mongodb://localhost:27017')
client = AsyncIOMotorClient(mongo_url)
db = client['freshwala_db']

# New categories based on catalog
categories_data = [
    {
        'id': '1',
        'name': 'Podulu (Spice Powders)',
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/c7042794e00fb94fe0259cdf06ab3404f96ea5298f35225d20b636cb5ab61897.jpg',
        'description': 'Traditional spice powders'
    },
    {
        'id': '2',
        'name': 'Dehydrated Powders',
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/671165bd5c8e1e95a053a6225617ddee2efaad9340e055ebf335b7811e167a98.jpg',
        'description': 'Onion, Garlic, Tomato, Ginger & more'
    },
    {
        'id': '3',
        'name': 'Dairy Products',
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/b9912d793bd70b01af9055bf8a39ae5b58bae11224261b2855bb1f1b607e0978.jpg',
        'description': 'Fresh Ghee, Butter, Paneer & more'
    },
    {
        'id': '4',
        'name': 'Papad',
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/5257ba4f708c813ebef34778f2f55906bc9c191b05524380101fbf93fa844c08.jpg',
        'description': 'Crispy homemade papads'
    },
    {
        'id': '5',
        'name': 'Pickles',
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/a6b2d212d8a33495e67beeff53848989da4f48512e8514fa07925c044065f8f6.jpg',
        'description': 'Spicy traditional pickles'
    },
    {
        'id': '6',
        'name': 'Batters',
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/5982790eee994a23a76fe85b8a506518cfd18573be007b4fb7d9f1693ca23a85.jpg',
        'description': 'Fresh Idli, Dosa & more batters'
    }
]

# All products from catalog
products_data = [
    # Podulu (Spice Powders)
    {
        'id': '1',
        'name': 'Kandi Powder',
        'category': 'Podulu (Spice Powders)',
        'categoryId': '1',
        'price': 100,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/c7042794e00fb94fe0259cdf06ab3404f96ea5298f35225d20b636cb5ab61897.jpg',
        'description': 'Traditional Kandi spice powder',
        'weight': '100g',
        'inStock': True,
        'rating': 4.5,
        'reviews': 45
    },
    {
        'id': '2',
        'name': 'Kobbari Powder',
        'category': 'Podulu (Spice Powders)',
        'categoryId': '1',
        'price': 50,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/8e1301fdb4aef45995f7548483640202dc4ec88707f86a99eb785c04e3984567.jpg',
        'description': 'Fresh coconut powder',
        'weight': '100g',
        'inStock': True,
        'rating': 4.6,
        'reviews': 38
    },
    {
        'id': '3',
        'name': 'Groundnut Powder',
        'category': 'Podulu (Spice Powders)',
        'categoryId': '1',
        'price': 50,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/af1202e7854c0b0561a747635f4d8e8fa47ea9d9e0213a81cb2e3c438c0129d6.jpg',
        'description': 'Roasted groundnut powder',
        'weight': '100g',
        'inStock': True,
        'rating': 4.4,
        'reviews': 32
    },
    {
        'id': '4',
        'name': 'Sesame Powder',
        'category': 'Podulu (Spice Powders)',
        'categoryId': '1',
        'price': 50,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/26b7e40eeabce95d1cc176a663c5c2d4d24f61c693f26e3d7fc27f5273499c05.jpg',
        'description': 'Roasted sesame powder',
        'weight': '100g',
        'inStock': True,
        'rating': 4.5,
        'reviews': 28
    },
    {
        'id': '5',
        'name': 'Coriander Powder',
        'category': 'Podulu (Spice Powders)',
        'categoryId': '1',
        'price': 50,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/945f0b47970414cc044faa121823c27751f86ce7868af344e66d1413a3807d15.jpg',
        'description': 'Fresh coriander powder',
        'weight': '100g',
        'inStock': True,
        'rating': 4.7,
        'reviews': 55
    },
    {
        'id': '6',
        'name': 'Curry Leaves Powder',
        'category': 'Podulu (Spice Powders)',
        'categoryId': '1',
        'price': 50,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/789321607d2850938d14bd037e2d87ca837d46d415797b88d8609ac69a931f2f.jpg',
        'description': 'Aromatic curry leaves powder',
        'weight': '100g',
        'inStock': True,
        'rating': 4.8,
        'reviews': 42
    },
    
    # Dehydrated Powders
    {
        'id': '7',
        'name': 'Carrot Powder',
        'category': 'Dehydrated Powders',
        'categoryId': '2',
        'price': 200,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/b72f94d6ca9debccca59006712f97712e9a309326f821e591ed8fef5d839bca4.jpg',
        'description': 'Dehydrated carrot powder',
        'weight': '100g',
        'inStock': True,
        'rating': 4.5,
        'reviews': 25
    },
    {
        'id': '8',
        'name': 'Beetroot Powder',
        'category': 'Dehydrated Powders',
        'categoryId': '2',
        'price': 200,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/6be38035bbf6ceb6e617823e22b7f13996872b34035da2cef37e42eae39d99e0.jpg',
        'description': 'Natural beetroot powder',
        'weight': '100g',
        'inStock': True,
        'rating': 4.6,
        'reviews': 30
    },
    {
        'id': '9',
        'name': 'Moringa Powder',
        'category': 'Dehydrated Powders',
        'categoryId': '2',
        'price': 250,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/1b64ca01811582fb8955aad6f206107209016567fdc27ef4f3314e952763a0fb.jpg',
        'description': 'Pure moringa leaf powder',
        'weight': '100g',
        'inStock': True,
        'rating': 4.9,
        'reviews': 48
    },
    {
        'id': '10',
        'name': 'Onion Powder',
        'category': 'Dehydrated Powders',
        'categoryId': '2',
        'price': 200,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/671165bd5c8e1e95a053a6225617ddee2efaad9340e055ebf335b7811e167a98.jpg',
        'description': 'Dehydrated onion powder',
        'weight': '100g',
        'inStock': True,
        'rating': 4.7,
        'reviews': 62
    },
    {
        'id': '11',
        'name': 'Tomato Powder',
        'category': 'Dehydrated Powders',
        'categoryId': '2',
        'price': 200,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/57c84995162af15b0ac2f2dcad8b4d618d27dd901a7c3025846cc6fabd2ccbfc.jpg',
        'description': 'Dehydrated tomato powder',
        'weight': '100g',
        'inStock': True,
        'rating': 4.5,
        'reviews': 38
    },
    {
        'id': '12',
        'name': 'Ginger Powder',
        'category': 'Dehydrated Powders',
        'categoryId': '2',
        'price': 200,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/0d2c964b3dde5c8a91877b11824dbb1914f42072de2b1e677dc1d5701322255e.jpg',
        'description': 'Pure ginger powder',
        'weight': '100g',
        'inStock': True,
        'rating': 4.8,
        'reviews': 52
    },
    
    # Dairy Products
    {
        'id': '13',
        'name': 'Pure Buffalo Ghee',
        'category': 'Dairy Products',
        'categoryId': '3',
        'price': 250,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/c857cada804ab238d79041a6fa91a6037edad6b98cd40bb923a77fa6b2b1afd0.jpg',
        'description': 'Pure homemade buffalo ghee',
        'weight': '250g',
        'inStock': True,
        'rating': 5.0,
        'reviews': 95
    },
    {
        'id': '14',
        'name': 'Fresh Butter',
        'category': 'Dairy Products',
        'categoryId': '3',
        'price': 150,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/4b28b7c78dcdf9c3b86e418f28d3f2c006033fa885ff04702ab427f3fb8f4fc0.jpg',
        'description': 'Creamy fresh butter',
        'weight': '250g',
        'inStock': True,
        'rating': 4.8,
        'reviews': 72
    },
    {
        'id': '15',
        'name': 'Fresh Paneer',
        'category': 'Dairy Products',
        'categoryId': '3',
        'price': 150,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/d98cb0096ceca1f179e48d96608f49488070adf2adfd8c07ca91e2389cacc3dc.jpg',
        'description': 'Soft homemade paneer',
        'weight': '250g',
        'inStock': True,
        'rating': 4.9,
        'reviews': 88
    },
    {
        'id': '16',
        'name': 'Fresh Malai',
        'category': 'Dairy Products',
        'categoryId': '3',
        'price': 100,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/8d993e60e3b35eed66c2b2da1609f31bb091a6586b29756ab6f6fc6018b24dff.jpg',
        'description': 'Rich fresh malai',
        'weight': '250g',
        'inStock': True,
        'rating': 4.7,
        'reviews': 65
    },
    {
        'id': '17',
        'name': 'Khova',
        'category': 'Dairy Products',
        'categoryId': '3',
        'price': 100,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/b246000946ffaafb87274b591a784e1eabe13aa6f5eda9bf6d5c1f8f30e5da0f.jpg',
        'description': 'Traditional khova',
        'weight': '250g',
        'inStock': True,
        'rating': 4.6,
        'reviews': 45
    },
    
    # Papad
    {
        'id': '18',
        'name': 'Home Made Papad',
        'category': 'Papad',
        'categoryId': '4',
        'price': 50,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/5257ba4f708c813ebef34778f2f55906bc9c191b05524380101fbf93fa844c08.jpg',
        'description': 'Traditional homemade papad',
        'weight': '250g',
        'inStock': True,
        'rating': 4.7,
        'reviews': 92
    },
    {
        'id': '19',
        'name': 'Masala Papad',
        'category': 'Papad',
        'categoryId': '4',
        'price': 50,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/91f6dbac36271676b5c0e8597f41d0678d2ac175cd0da0691c07c693cdca8310.jpg',
        'description': 'Spicy masala papad',
        'weight': '250g',
        'inStock': True,
        'rating': 4.8,
        'reviews': 78
    },
    {
        'id': '20',
        'name': 'Urad Dal Papad',
        'category': 'Papad',
        'categoryId': '4',
        'price': 50,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/4c146e8be7afa22c4ad760766421e17126f16692740e08ae31eb86f7417fda35.jpg',
        'description': 'Classic urad dal papad',
        'weight': '250g',
        'inStock': True,
        'rating': 4.6,
        'reviews': 85
    },
    {
        'id': '21',
        'name': 'Moong Dal Papad',
        'category': 'Papad',
        'categoryId': '4',
        'price': 50,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/ba1f9de836e3d2cd2e1140808137ed4815ca2a58567527a57ab70ba1113b1e12.jpg',
        'description': 'Crispy moong dal papad',
        'weight': '250g',
        'inStock': True,
        'rating': 4.5,
        'reviews': 68
    },
    {
        'id': '22',
        'name': 'Tomato Papad',
        'category': 'Papad',
        'categoryId': '4',
        'price': 50,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/284b8d4f99f4b0f0478bd585cbf929532c370e99f5e475a030f06b736cd9089d.jpg',
        'description': 'Tangy tomato papad',
        'weight': '250g',
        'inStock': True,
        'rating': 4.7,
        'reviews': 72
    },
    {
        'id': '23',
        'name': 'Sabudana Papad',
        'category': 'Papad',
        'categoryId': '4',
        'price': 50,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/cff9633ad24eb068d4bd0ad876f1da3907706a4ab1405bfa2a7120af066c5ca0.jpg',
        'description': 'Light sabudana papad',
        'weight': '250g',
        'inStock': True,
        'rating': 4.6,
        'reviews': 58
    },
    {
        'id': '24',
        'name': 'Green Chilli Papad',
        'category': 'Papad',
        'categoryId': '4',
        'price': 50,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/7ca13a2e8f4123e6d640657914d4b842035105b35bab5c8d57cef59e89f49f66.jpg',
        'description': 'Spicy green chilli papad',
        'weight': '250g',
        'inStock': True,
        'rating': 4.8,
        'reviews': 64
    },
    
    # Pickles
    {
        'id': '25',
        'name': 'Mango Pickle',
        'category': 'Pickles',
        'categoryId': '5',
        'price': 150,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/a6b2d212d8a33495e67beeff53848989da4f48512e8514fa07925c044065f8f6.jpg',
        'description': 'Freshwala Mango Pickle - Traditional Andhra style',
        'weight': '250g',
        'inStock': True,
        'rating': 4.9,
        'reviews': 145
    },
    {
        'id': '26',
        'name': 'Lemon Pickle',
        'category': 'Pickles',
        'categoryId': '5',
        'price': 150,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/e01c15d6742a0aeb540be585d96e56c625dfb926f1b90df0370373b1146eed1e.jpg',
        'description': 'Tangy lemon pickle',
        'weight': '250g',
        'inStock': True,
        'rating': 4.7,
        'reviews': 98
    },
    {
        'id': '27',
        'name': 'Amla Pickle',
        'category': 'Pickles',
        'categoryId': '5',
        'price': 150,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/fff8c33024aef492424a67eac76adbc7b993ccffb18064f891b835dd2c7df0f9.jpg',
        'description': 'Healthy amla pickle',
        'weight': '250g',
        'inStock': True,
        'rating': 4.8,
        'reviews': 82
    },
    {
        'id': '28',
        'name': 'Tamarind Pickle',
        'category': 'Pickles',
        'categoryId': '5',
        'price': 150,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/3feffb78fb573ede8bdbdb5735ec42a9f9ff0c56666aa174ede69e4a45f20d91.jpg',
        'description': 'Sweet and sour tamarind pickle',
        'weight': '250g',
        'inStock': True,
        'rating': 4.6,
        'reviews': 75
    },
    {
        'id': '29',
        'name': 'Tomato Pickle',
        'category': 'Pickles',
        'categoryId': '5',
        'price': 150,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/f277269b0335c2865dde22083b316888badeb1fb12cf804f0782c260ba50566c.jpg',
        'description': 'Tangy tomato pickle',
        'weight': '250g',
        'inStock': True,
        'rating': 4.5,
        'reviews': 68
    },
    {
        'id': '30',
        'name': 'Gongura Pickle',
        'category': 'Pickles',
        'categoryId': '5',
        'price': 150,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/3f3d2ebcf666153c353ff6bdc7f815f05382fc9414a2e85daabf3e3270bec95a.jpg',
        'description': 'Traditional gongura pickle',
        'weight': '250g',
        'inStock': True,
        'rating': 4.9,
        'reviews': 128
    },
    {
        'id': '31',
        'name': 'Drumstick Pickle',
        'category': 'Pickles',
        'categoryId': '5',
        'price': 150,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/7d652eed773daca23e9ee3606f1fcb5a10fc68c969a9f7b7d997102630f10966.jpg',
        'description': 'Unique drumstick pickle',
        'weight': '250g',
        'inStock': True,
        'rating': 4.7,
        'reviews': 54
    },
    {
        'id': '32',
        'name': 'Pudina Pickle',
        'category': 'Pickles',
        'categoryId': '5',
        'price': 150,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/7b073db255ef6c7beabc8d6ff1f78468749e509c96b1de31d7ba5fdda7ec55ab.jpg',
        'description': 'Refreshing mint pickle',
        'weight': '250g',
        'inStock': True,
        'rating': 4.6,
        'reviews': 62
    },
    {
        'id': '33',
        'name': 'Ginger Pickle',
        'category': 'Pickles',
        'categoryId': '5',
        'price': 150,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/a9d9813b8e0410f8c37d17cf70d0fb6d8d916d9de011941dcbc2c07c98f9df01.jpg',
        'description': 'Spicy ginger pickle',
        'weight': '250g',
        'inStock': True,
        'rating': 4.7,
        'reviews': 71
    },
    {
        'id': '34',
        'name': 'Garlic Pickle',
        'category': 'Pickles',
        'categoryId': '5',
        'price': 150,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/afef77da2b89ed4cdb92064aded22012a640d353722bc92724232bc0c0b7b025.jpg',
        'description': 'Aromatic garlic pickle',
        'weight': '250g',
        'inStock': True,
        'rating': 4.8,
        'reviews': 84
    },
    {
        'id': '35',
        'name': 'Coriander Pickle',
        'category': 'Pickles',
        'categoryId': '5',
        'price': 150,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/bf57fc9a37cc2da4c7f4de7ce660f132ac69c173ead23f56bf4fc5aaf5f7f3f4.jpg',
        'description': 'Fresh coriander pickle',
        'weight': '250g',
        'inStock': True,
        'rating': 4.5,
        'reviews': 48
    },
    {
        'id': '36',
        'name': 'Curry Leaves Pickle',
        'category': 'Pickles',
        'categoryId': '5',
        'price': 150,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/85c76cda38cef19e8a3f90c22289218d4bf2cf329e5fa56dfcebd152ac103237.jpg',
        'description': 'Aromatic curry leaves pickle',
        'weight': '250g',
        'inStock': True,
        'rating': 4.6,
        'reviews': 56
    },
    {
        'id': '37',
        'name': 'Brinjal Pickle',
        'category': 'Pickles',
        'categoryId': '5',
        'price': 150,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/0c57be5c444d197f31210e36891e42639345203ef45475563f7e4692a883fc3e.jpg',
        'description': 'Tasty brinjal pickle',
        'weight': '250g',
        'inStock': True,
        'rating': 4.7,
        'reviews': 63
    },
    {
        'id': '38',
        'name': 'Chicken Pickle',
        'category': 'Pickles',
        'categoryId': '5',
        'price': 300,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/79fe0655344adbbf70d631478d4e1cb5a2732c4b61c579a1ec44b1ec433b36f1.jpg',
        'description': 'Spicy chicken pickle',
        'weight': '250g',
        'inStock': True,
        'rating': 4.9,
        'reviews': 112
    },
    {
        'id': '39',
        'name': 'Mutton Pickle',
        'category': 'Pickles',
        'categoryId': '5',
        'price': 450,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/4fc05bc5979c6efdeae8cadd00ee91a6b56715464cffa8bb3b4af95ce526e746.jpg',
        'description': 'Rich mutton pickle',
        'weight': '250g',
        'inStock': True,
        'rating': 5.0,
        'reviews': 98
    },
    {
        'id': '40',
        'name': 'Fish Pickle',
        'category': 'Pickles',
        'categoryId': '5',
        'price': 250,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/1a05cd9311699a6c059b076e911eecc40f5df5a3225a943127e0d51d7a100021.jpg',
        'description': 'Coastal fish pickle',
        'weight': '250g',
        'inStock': True,
        'rating': 4.8,
        'reviews': 76
    },
    {
        'id': '41',
        'name': 'Prawns Pickle',
        'category': 'Pickles',
        'categoryId': '5',
        'price': 400,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/cd6ecf3f16c82142b7617dc9a0fc228c66ae66e50f933556afe96510b0aa39e4.jpg',
        'description': 'Delicious prawns pickle',
        'weight': '250g',
        'inStock': True,
        'rating': 4.9,
        'reviews': 88
    },
    {
        'id': '42',
        'name': 'Beef Pickle',
        'category': 'Pickles',
        'categoryId': '5',
        'price': 350,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/e8734ef4073989a4e4bb447dd1a5579b8a12238737610c30f9f50c0f4f9fd82a.jpg',
        'description': 'Spicy beef pickle',
        'weight': '250g',
        'inStock': True,
        'rating': 4.8,
        'reviews': 72
    },
    
    # Batters
    {
        'id': '43',
        'name': 'Idli Batter',
        'category': 'Batters',
        'categoryId': '6',
        'price': 70,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/5982790eee994a23a76fe85b8a506518cfd18573be007b4fb7d9f1693ca23a85.jpg',
        'description': 'Freshwala Idli Batter - Soft and fluffy',
        'weight': '1kg',
        'inStock': True,
        'rating': 4.9,
        'reviews': 185
    },
    {
        'id': '44',
        'name': 'Dosa Batter',
        'category': 'Batters',
        'categoryId': '6',
        'price': 70,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/4ef626419f8dc3245582946290ebfac659345e7999ec7c65a4ae67c189eaa3f6.jpg',
        'description': 'Home Made Fresh Dosa Batter - Crispy dosas',
        'weight': '1kg',
        'inStock': True,
        'rating': 4.8,
        'reviews': 172
    },
    {
        'id': '45',
        'name': 'Gare Batter',
        'category': 'Batters',
        'categoryId': '6',
        'price': 100,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/937bd8ee9ae6fa16d0c09ec80dfdf87a26f68628aade0cd28e8c3f6f45376c4b.jpg',
        'description': 'Traditional Gare batter',
        'weight': '1kg',
        'inStock': True,
        'rating': 4.7,
        'reviews': 64
    },
    {
        'id': '46',
        'name': 'Pesarattu Batter',
        'category': 'Batters',
        'categoryId': '6',
        'price': 90,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/7b270005b2ff6893f1f3c9fd6e79917a6df78dd35d57fa04db32dbc518f992a4.jpg',
        'description': 'Healthy pesarattu batter',
        'weight': '1kg',
        'inStock': True,
        'rating': 4.8,
        'reviews': 96
    },
    {
        'id': '47',
        'name': 'Millet Batter',
        'category': 'Batters',
        'categoryId': '6',
        'price': 100,
        'originalPrice': None,
        'image': 'https://customer-assets.emergentagent.com/job_mobile-fresh/artifacts/images/2370078f185c8bdad558f2075dcb7cc80855e6544da08a6fecaa5f8f333cd4e1.jpg',
        'description': 'Freshwala Millet Batter - Nutritious',
        'weight': '1kg',
        'inStock': True,
        'rating': 4.9,
        'reviews': 78
    }
]

async def update_database():
    print("Clearing existing data...")
    await db.categories.delete_many({})
    await db.products.delete_many({})
    
    print("Inserting new categories...")
    await db.categories.insert_many(categories_data)
    print(f"Inserted {len(categories_data)} categories")
    
    print("Inserting new products...")
    await db.products.insert_many(products_data)
    print(f"Inserted {len(products_data)} products")
    
    print("Database updated successfully!")
    client.close()

if __name__ == "__main__":
    asyncio.run(update_database())
