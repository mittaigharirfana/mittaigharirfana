# Seed data for Freshwala database

categories_data = [
    {
        'id': '1',
        'name': 'Podulu',
        'image': 'https://images.unsplash.com/photo-1698557048177-a460bb415177',
        'description': 'Traditional spice powders'
    },
    {
        'id': '2',
        'name': 'Dehydrated Powders',
        'image': 'https://images.unsplash.com/photo-1656497119922-068c6a5e1193?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDQ2Mzl8MHwxfHNlYXJjaHwyfHxpbmRpYW4lMjBzcGljZXN8ZW58MHx8fHwxNzYxMjExNzM3fDA&ixlib=rb-4.1.0&q=85',
        'description': 'Onion, Garlic & more'
    },
    {
        'id': '3',
        'name': 'Dairy Products',
        'image': 'https://images.unsplash.com/photo-1635436338433-89747d0ca0ef',
        'description': 'Fresh Ghee & Paneer'
    },
    {
        'id': '4',
        'name': 'Papad',
        'image': 'https://images.pexels.com/photos/8818667/pexels-photo-8818667.jpeg',
        'description': 'Crispy homemade papads'
    },
    {
        'id': '5',
        'name': 'Pickles',
        'image': 'https://images.unsplash.com/photo-1617854307432-13950e24ba07',
        'description': 'Spicy traditional pickles'
    },
    {
        'id': '6',
        'name': 'Batters',
        'image': 'https://images.unsplash.com/photo-1589301760014-d929f3979dbc',
        'description': 'Fresh Idli & Dosa batter'
    }
]

products_data = [
    {
        'id': '1',
        'name': 'Avakaya Pickle',
        'category': 'Pickles',
        'categoryId': '5',
        'price': 250,
        'originalPrice': 300,
        'image': 'https://images.unsplash.com/photo-1617854307432-13950e24ba07?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2Njl8MHwxfHNlYXJjaHwxfHxpbmRpYW4lMjBwaWNrbGVzfGVufDB8fHx8MTc2MTIxMTczMXww&ixlib=rb-4.1.0&q=85',
        'description': 'Spicy traditional Andhra mango pickle made with authentic recipes',
        'weight': '500g',
        'inStock': True,
        'rating': 4.5,
        'reviews': 120
    },
    {
        'id': '2',
        'name': 'Gongura Pickle',
        'category': 'Pickles',
        'categoryId': '5',
        'price': 200,
        'originalPrice': 250,
        'image': 'https://images.unsplash.com/photo-1617854307432-13950e24ba07?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2Njl8MHwxfHNlYXJjaHwxfHxpbmRpYW4lMjBwaWNrbGVzfGVufDB8fHx8MTc2MTIxMTczMXww&ixlib=rb-4.1.0&q=85',
        'description': 'Tangy sorrel leaves pickle, a Telangana favorite',
        'weight': '500g',
        'inStock': True,
        'rating': 4.8,
        'reviews': 95
    },
    {
        'id': '3',
        'name': 'Pure Cow Ghee',
        'category': 'Dairy Products',
        'categoryId': '3',
        'price': 600,
        'originalPrice': 700,
        'image': 'https://images.unsplash.com/photo-1581600140682-d4e68c8cde32?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDQ2Mzl8MHwxfHNlYXJjaHwzfHxpbmRpYW4lMjBzcGljZXN8ZW58MHx8fHwxNzYxMjExNzM3fDA&ixlib=rb-4.1.0&q=85',
        'description': 'Fresh homemade cow ghee, pure and healthy',
        'weight': '1kg',
        'inStock': True,
        'rating': 5.0,
        'reviews': 200
    },
    {
        'id': '4',
        'name': 'Idli Batter',
        'category': 'Batters',
        'categoryId': '6',
        'price': 80,
        'originalPrice': 100,
        'image': 'https://images.pexels.com/photos/14132112/pexels-photo-14132112.jpeg',
        'description': 'Freshly ground idli batter, ready to use',
        'weight': '1kg',
        'inStock': True,
        'rating': 4.7,
        'reviews': 150
    },
    {
        'id': '5',
        'name': 'Dosa Batter',
        'category': 'Batters',
        'categoryId': '6',
        'price': 90,
        'originalPrice': 110,
        'image': 'https://images.pexels.com/photos/14132112/pexels-photo-14132112.jpeg',
        'description': 'Crispy dosa batter, traditional recipe',
        'weight': '1kg',
        'inStock': True,
        'rating': 4.6,
        'reviews': 130
    },
    {
        'id': '6',
        'name': 'Garlic Powder',
        'category': 'Dehydrated Powders',
        'categoryId': '2',
        'price': 120,
        'originalPrice': 150,
        'image': 'https://images.unsplash.com/photo-1656497119922-068c6a5e1193?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDQ2Mzl8MHwxfHNlYXJjaHwyfHxpbmRpYW4lMjBzcGljZXN8ZW58MHx8fHwxNzYxMjExNzM3fDA&ixlib=rb-4.1.0&q=85',
        'description': 'Pure dehydrated garlic powder',
        'weight': '200g',
        'inStock': True,
        'rating': 4.4,
        'reviews': 80
    },
    {
        'id': '7',
        'name': 'Onion Powder',
        'category': 'Dehydrated Powders',
        'categoryId': '2',
        'price': 100,
        'originalPrice': 130,
        'image': 'https://images.unsplash.com/photo-1656497119922-068c6a5e1193?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDQ2Mzl8MHwxfHNlYXJjaHwyfHxpbmRpYW4lMjBzcGljZXN8ZW58MHx8fHwxNzYxMjExNzM3fDA&ixlib=rb-4.1.0&q=85',
        'description': 'Dehydrated onion powder for easy cooking',
        'weight': '200g',
        'inStock': True,
        'rating': 4.3,
        'reviews': 65
    },
    {
        'id': '8',
        'name': 'Rice Papad',
        'category': 'Papad',
        'categoryId': '4',
        'price': 60,
        'originalPrice': 80,
        'image': 'https://images.pexels.com/photos/9266190/pexels-photo-9266190.jpeg',
        'description': 'Crispy rice papads, homemade quality',
        'weight': '250g',
        'inStock': True,
        'rating': 4.5,
        'reviews': 110
    },
    {
        'id': '9',
        'name': 'Guntur Karam Podi',
        'category': 'Podulu',
        'categoryId': '1',
        'price': 150,
        'originalPrice': 180,
        'image': 'https://images.unsplash.com/photo-1596040033229-a9821ebd058d?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDQ2Mzl8MHwxfHNlYXJjaHwxfHxpbmRpYW4lMjBzcGljZXN8ZW58MHx8fHwxNzYxMjExNzM3fDA&ixlib=rb-4.1.0&q=85',
        'description': 'Spicy Guntur chili powder',
        'weight': '250g',
        'inStock': True,
        'rating': 4.9,
        'reviews': 180
    },
    {
        'id': '10',
        'name': 'Idli Podi',
        'category': 'Podulu',
        'categoryId': '1',
        'price': 130,
        'originalPrice': 160,
        'image': 'https://images.unsplash.com/photo-1596040033229-a9821ebd058d?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDQ2Mzl8MHwxfHNlYXJjaHwxfHxpbmRpYW4lMjBzcGljZXN8ZW58MHx8fHwxNzYxMjExNzM3fDA&ixlib=rb-4.1.0&q=85',
        'description': 'Traditional idli podi with sesame and lentils',
        'weight': '200g',
        'inStock': True,
        'rating': 4.7,
        'reviews': 140
    },
    {
        'id': '11',
        'name': 'Fresh Paneer',
        'category': 'Dairy Products',
        'categoryId': '3',
        'price': 180,
        'originalPrice': 220,
        'image': 'https://images.unsplash.com/photo-1581600140682-d4e68c8cde32?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDQ2Mzl8MHwxfHNlYXJjaHwzfHxpbmRpYW4lMjBzcGljZXN8ZW58MHx8fHwxNzYxMjExNzM3fDA&ixlib=rb-4.1.0&q=85',
        'description': 'Soft homemade paneer, made fresh daily',
        'weight': '500g',
        'inStock': True,
        'rating': 4.8,
        'reviews': 160
    },
    {
        'id': '12',
        'name': 'Tomato Pickle',
        'category': 'Pickles',
        'categoryId': '5',
        'price': 180,
        'originalPrice': 220,
        'image': 'https://images.unsplash.com/photo-1617854307432-13950e24ba07?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2Njl8MHwxfHNlYXJjaHwxfHxpbmRpYW4lMjBwaWNrbGVzfGVufDB8fHx8MTc2MTIxMTczMXww&ixlib=rb-4.1.0&q=85',
        'description': 'Tangy tomato pickle with aromatic spices',
        'weight': '500g',
        'inStock': True,
        'rating': 4.4,
        'reviews': 75
    }
]
