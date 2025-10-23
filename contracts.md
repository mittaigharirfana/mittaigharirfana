# Freshwala E-commerce Backend Contracts

## API Endpoints

### 1. Authentication
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `GET /api/auth/profile` - Get user profile
- `PUT /api/auth/profile` - Update user profile

### 2. Products
- `GET /api/products` - Get all products (with filters)
- `GET /api/products/:id` - Get single product
- `GET /api/categories` - Get all categories

### 3. Orders
- `POST /api/orders/create` - Create order and Razorpay order
  - Request: { amount, items, shippingAddress }
  - Response: { orderId, razorpayOrderId }
- `POST /api/orders/verify-payment` - Verify Razorpay payment
  - Request: { orderId, razorpayPaymentId, razorpayOrderId, razorpaySignature }
  - Response: { success: boolean }
- `GET /api/orders` - Get user's orders
- `GET /api/orders/:orderId` - Get specific order

### 4. Cart & Wishlist
- Cart is handled on frontend (localStorage)
- Wishlist is handled on frontend (localStorage)

## Database Models

### User
- _id
- name
- email
- password (hashed)
- phone
- address
- createdAt

### Product
- _id
- name
- category
- categoryId
- price
- originalPrice
- image
- description
- weight
- inStock
- rating
- reviews

### Order
- _id
- orderId (generated)
- userId
- items (array)
- totalAmount
- shippingAddress
- razorpayOrderId
- razorpayPaymentId
- status (pending, processing, delivered, cancelled)
- createdAt
- updatedAt

## Mocked Data in Frontend (mock.js)
- Categories: 6 categories with images
- Products: 12 products with details
- Testimonials: 4 customer reviews
- Features: 4 "Why Choose Us" items

## Frontend-Backend Integration
1. Products are stored in MongoDB, fetched via API
2. User authentication with JWT
3. Orders created with Razorpay integration
4. Payment verification on backend
5. Order status tracking

## Razorpay Integration
- API Keys stored in backend .env
- Order creation with Razorpay API
- Payment verification with signature validation
- Order status updates after successful payment
