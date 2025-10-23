import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Minus, Plus, Trash2, ShoppingBag } from 'lucide-react';
import { Button } from '../components/ui/button';
import { useCart } from '../contexts/CartContext';
import { useAuth } from '../contexts/AuthContext';
import { toast } from '../hooks/use-toast';

const Cart = () => {
  const navigate = useNavigate();
  const { cartItems, updateQuantity, removeFromCart, getCartTotal } = useCart();
  const { isAuthenticated } = useAuth();

  const handleCheckout = () => {
    if (!isAuthenticated()) {
      toast({
        title: 'Login Required',
        description: 'Please login to proceed with checkout.',
        variant: 'destructive',
      });
      navigate('/login?redirect=/checkout');
      return;
    }
    navigate('/checkout');
  };

  const handleRemove = (product) => {
    removeFromCart(product.id);
    toast({
      title: 'Removed from cart',
      description: `${product.name} has been removed from your cart.`,
    });
  };

  if (cartItems.length === 0) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center py-12">
          <ShoppingBag size={64} className="mx-auto text-gray-400 mb-4" />
          <h2 className="text-2xl font-bold text-gray-900 mb-2">Your cart is empty</h2>
          <p className="text-gray-600 mb-6">Start shopping and add items to your cart!</p>
          <Button
            onClick={() => navigate('/shop')}
            className="bg-orange-500 hover:bg-orange-600"
          >
            Start Shopping
          </Button>
        </div>
      </div>
    );
  }

  const subtotal = getCartTotal();
  const deliveryCharge = subtotal >= 500 ? 0 : 40;
  const total = subtotal + deliveryCharge;

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">Shopping Cart</h1>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Cart Items */}
          <div className="lg:col-span-2 space-y-4">
            {cartItems.map((item) => (
              <div key={item.id} className="bg-white rounded-lg shadow-md p-6">
                <div className="flex items-start space-x-4">
                  {/* Image */}
                  <Link to={`/product/${item.id}`} className="flex-shrink-0">
                    <img
                      src={item.image}
                      alt={item.name}
                      className="w-24 h-24 object-cover rounded-lg"
                    />
                  </Link>

                  {/* Details */}
                  <div className="flex-1 min-w-0">
                    <Link to={`/product/${item.id}`}>
                      <h3 className="text-lg font-semibold text-gray-900 hover:text-orange-600">
                        {item.name}
                      </h3>
                    </Link>
                    <p className="text-sm text-gray-600 mt-1">{item.category}</p>
                    {item.weight && (
                      <p className="text-sm text-gray-500 mt-1">{item.weight}</p>
                    )}
                    <p className="text-xl font-bold text-gray-900 mt-2">₹{item.price}</p>
                  </div>

                  {/* Quantity & Remove */}
                  <div className="flex flex-col items-end space-y-4">
                    <button
                      onClick={() => handleRemove(item)}
                      className="text-red-500 hover:text-red-700"
                    >
                      <Trash2 size={20} />
                    </button>

                    <div className="flex items-center border rounded-lg">
                      <button
                        onClick={() => updateQuantity(item.id, item.quantity - 1)}
                        className="p-2 hover:bg-gray-100"
                      >
                        <Minus size={16} />
                      </button>
                      <span className="px-4 font-semibold">{item.quantity}</span>
                      <button
                        onClick={() => updateQuantity(item.id, item.quantity + 1)}
                        className="p-2 hover:bg-gray-100"
                      >
                        <Plus size={16} />
                      </button>
                    </div>

                    <p className="text-lg font-bold text-gray-900">
                      ₹{item.price * item.quantity}
                    </p>
                  </div>
                </div>
              </div>
            ))}
          </div>

          {/* Order Summary */}
          <div className="lg:col-span-1">
            <div className="bg-white rounded-lg shadow-md p-6 sticky top-24">
              <h2 className="text-xl font-bold text-gray-900 mb-6">Order Summary</h2>
              
              <div className="space-y-4">
                <div className="flex justify-between text-gray-700">
                  <span>Subtotal</span>
                  <span className="font-semibold">₹{subtotal}</span>
                </div>
                
                <div className="flex justify-between text-gray-700">
                  <span>Delivery Charges</span>
                  <span className="font-semibold">
                    {deliveryCharge === 0 ? (
                      <span className="text-green-600">FREE</span>
                    ) : (
                      `₹${deliveryCharge}`
                    )}
                  </span>
                </div>

                {subtotal < 500 && (
                  <p className="text-sm text-orange-600">
                    Add ₹{500 - subtotal} more for FREE delivery!
                  </p>
                )}

                <div className="border-t pt-4">
                  <div className="flex justify-between text-lg font-bold text-gray-900">
                    <span>Total</span>
                    <span>₹{total}</span>
                  </div>
                </div>

                <Button
                  onClick={handleCheckout}
                  className="w-full bg-orange-500 hover:bg-orange-600 text-white py-6 text-lg font-semibold"
                >
                  Proceed to Checkout
                </Button>

                <Link to="/shop">
                  <Button variant="outline" className="w-full">
                    Continue Shopping
                  </Button>
                </Link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Cart;
