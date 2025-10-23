import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { ShoppingCart, Heart, Minus, Plus, Truck, Shield, RefreshCw } from 'lucide-react';
import { Button } from '../components/ui/button';
import { useCart } from '../contexts/CartContext';
import { useWishlist } from '../contexts/WishlistContext';
import { toast } from '../hooks/use-toast';
import ProductCard from '../components/ProductCard';
import axios from 'axios';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

const ProductDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [product, setProduct] = useState(null);
  const [relatedProducts, setRelatedProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const { addToCart } = useCart();
  const { isInWishlist, toggleWishlist } = useWishlist();
  const [quantity, setQuantity] = useState(1);

  useEffect(() => {
    const fetchProduct = async () => {
      try {
        const response = await axios.get(`${API}/products/${id}`);
        setProduct(response.data);
        
        // Fetch related products
        const relatedRes = await axios.get(`${API}/products?category=${response.data.category}`);
        const related = relatedRes.data.filter(p => p.id !== id).slice(0, 4);
        setRelatedProducts(related);
      } catch (error) {
        console.error('Error fetching product:', error);
      } finally {
        setLoading(false);
      }
    };
    fetchProduct();
  }, [id]);

  if (!product) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">Product not found</h2>
          <Button onClick={() => navigate('/shop')} className="bg-orange-500 hover:bg-orange-600">
            Back to Shop
          </Button>
        </div>
      </div>
    );
  }

  const relatedProducts = products
    .filter(p => p.categoryId === product.categoryId && p.id !== product.id)
    .slice(0, 4);

  const inWishlist = isInWishlist(product.id);
  const discount = product.originalPrice
    ? Math.round(((product.originalPrice - product.price) / product.originalPrice) * 100)
    : 0;

  const handleAddToCart = () => {
    addToCart(product, quantity);
    toast({
      title: 'Added to cart',
      description: `${quantity} × ${product.name} added to your cart.`,
    });
  };

  const handleBuyNow = () => {
    addToCart(product, quantity);
    navigate('/cart');
  };

  const handleToggleWishlist = () => {
    toggleWishlist(product);
    toast({
      title: inWishlist ? 'Removed from wishlist' : 'Added to wishlist',
      description: inWishlist
        ? `${product.name} removed from wishlist.`
        : `${product.name} added to wishlist.`,
    });
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Breadcrumb */}
        <nav className="text-sm text-gray-600 mb-6">
          <button onClick={() => navigate('/')} className="hover:text-orange-600">Home</button>
          <span className="mx-2">/</span>
          <button onClick={() => navigate('/shop')} className="hover:text-orange-600">Shop</button>
          <span className="mx-2">/</span>
          <span className="text-gray-900">{product.name}</span>
        </nav>

        {/* Product Details */}
        <div className="bg-white rounded-lg shadow-md p-6 md:p-8 mb-12">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-12">
            {/* Image */}
            <div className="relative">
              <img
                src={product.image}
                alt={product.name}
                className="w-full rounded-lg shadow-lg"
              />
              {discount > 0 && (
                <div className="absolute top-4 left-4 bg-red-500 text-white px-4 py-2 rounded-full font-bold">
                  {discount}% OFF
                </div>
              )}
            </div>

            {/* Info */}
            <div className="space-y-6">
              <div>
                <p className="text-orange-600 font-semibold mb-2">{product.category}</p>
                <h1 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
                  {product.name}
                </h1>
                
                {/* Rating */}
                {product.rating && (
                  <div className="flex items-center mb-4">
                    <div className="flex text-yellow-400">
                      {[...Array(5)].map((_, i) => (
                        <svg
                          key={i}
                          className={`w-5 h-5 ${i < Math.floor(product.rating) ? 'fill-current' : 'fill-gray-300'}`}
                          viewBox="0 0 20 20"
                        >
                          <path d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z" />
                        </svg>
                      ))}
                    </div>
                    <span className="text-gray-600 ml-2">({product.reviews} reviews)</span>
                  </div>
                )}

                <p className="text-gray-700 leading-relaxed">{product.description}</p>
              </div>

              {/* Price */}
              <div className="border-t border-b py-4">
                <div className="flex items-center space-x-4">
                  <span className="text-4xl font-bold text-gray-900">₹{product.price}</span>
                  {product.originalPrice && (
                    <span className="text-xl text-gray-500 line-through">₹{product.originalPrice}</span>
                  )}
                </div>
                {product.weight && (
                  <p className="text-gray-600 mt-2">Pack Size: {product.weight}</p>
                )}
                <p className={`mt-2 font-semibold ${product.inStock ? 'text-green-600' : 'text-red-600'}`}>
                  {product.inStock ? 'In Stock' : 'Out of Stock'}
                </p>
              </div>

              {/* Quantity Selector */}
              <div className="space-y-4">
                <div className="flex items-center space-x-4">
                  <span className="text-gray-700 font-semibold">Quantity:</span>
                  <div className="flex items-center border rounded-lg">
                    <button
                      onClick={() => setQuantity(Math.max(1, quantity - 1))}
                      className="p-2 hover:bg-gray-100"
                    >
                      <Minus size={20} />
                    </button>
                    <span className="px-6 font-semibold">{quantity}</span>
                    <button
                      onClick={() => setQuantity(quantity + 1)}
                      className="p-2 hover:bg-gray-100"
                    >
                      <Plus size={20} />
                    </button>
                  </div>
                </div>

                {/* Action Buttons */}
                <div className="flex flex-col sm:flex-row gap-4">
                  <Button
                    onClick={handleAddToCart}
                    disabled={!product.inStock}
                    className="flex-1 bg-orange-500 hover:bg-orange-600 text-white py-6 text-lg"
                  >
                    <ShoppingCart size={20} className="mr-2" />
                    Add to Cart
                  </Button>
                  <Button
                    onClick={handleBuyNow}
                    disabled={!product.inStock}
                    className="flex-1 bg-green-600 hover:bg-green-700 text-white py-6 text-lg"
                  >
                    Buy Now
                  </Button>
                  <Button
                    onClick={handleToggleWishlist}
                    variant="outline"
                    className="py-6 px-6"
                  >
                    <Heart
                      size={20}
                      className={inWishlist ? 'fill-red-500 text-red-500' : ''}
                    />
                  </Button>
                </div>
              </div>

              {/* Features */}
              <div className="border-t pt-6 space-y-3">
                <div className="flex items-center text-gray-700">
                  <Truck size={20} className="text-orange-500 mr-3" />
                  <span>Free delivery on orders above ₹500</span>
                </div>
                <div className="flex items-center text-gray-700">
                  <Shield size={20} className="text-orange-500 mr-3" />
                  <span>100% Quality Guaranteed</span>
                </div>
                <div className="flex items-center text-gray-700">
                  <RefreshCw size={20} className="text-orange-500 mr-3" />
                  <span>Easy Returns within 7 days</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Related Products */}
        {relatedProducts.length > 0 && (
          <div>
            <h2 className="text-2xl font-bold text-gray-900 mb-6">Related Products</h2>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
              {relatedProducts.map((product) => (
                <ProductCard key={product.id} product={product} />
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default ProductDetail;
