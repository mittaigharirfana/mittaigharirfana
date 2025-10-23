import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Search, ShoppingCart, Heart, User, Menu, X } from 'lucide-react';
import { useCart } from '../contexts/CartContext';
import { useWishlist } from '../contexts/WishlistContext';
import { useAuth } from '../contexts/AuthContext';
import { Button } from './ui/button';
import { Input } from './ui/input';
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from './ui/dropdown-menu';

const Header = () => {
  const navigate = useNavigate();
  const { getCartCount } = useCart();
  const { wishlistItems } = useWishlist();
  const { user, logout } = useAuth();
  const [searchQuery, setSearchQuery] = useState('');
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const handleSearch = (e) => {
    e.preventDefault();
    if (searchQuery.trim()) {
      navigate(`/shop?search=${searchQuery}`);
      setSearchQuery('');
    }
  };

  const handleLogout = () => {
    logout();
    navigate('/');
  };

  return (
    <>
      {/* Announcement Bar */}
      <div className="bg-gradient-to-r from-orange-500 to-amber-500 text-white py-2 overflow-hidden">
        <div className="animate-marquee whitespace-nowrap">
          <span className="mx-8">From Papads to Powders - Everything Fresh in One Place</span>
          <span className="mx-8">Fresh Dairy & Crispy Papads - Order Now!</span>
          <span className="mx-8">From Papads to Powders - Everything Fresh in One Place</span>
          <span className="mx-8">Fresh Dairy & Crispy Papads - Order Now!</span>
        </div>
      </div>

      {/* Main Header */}
      <header className="bg-white shadow-sm sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-20">
            {/* Mobile Menu Button */}
            <button
              className="md:hidden p-2"
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            >
              {mobileMenuOpen ? <X size={24} /> : <Menu size={24} />}
            </button>

            {/* Left Navigation */}
            <nav className="hidden md:flex items-center space-x-8">
              <Link to="/" className="text-gray-700 hover:text-orange-600 transition-colors font-medium">
                Home
              </Link>
              <DropdownMenu>
                <DropdownMenuTrigger className="text-gray-700 hover:text-orange-600 transition-colors font-medium">
                  Shop
                </DropdownMenuTrigger>
                <DropdownMenuContent>
                  <DropdownMenuItem onClick={() => navigate('/shop')}>
                    All Products
                  </DropdownMenuItem>
                  <DropdownMenuItem onClick={() => navigate('/shop?category=Pickles')}>
                    Pickles
                  </DropdownMenuItem>
                  <DropdownMenuItem onClick={() => navigate('/shop?category=Batters')}>
                    Batters
                  </DropdownMenuItem>
                  <DropdownMenuItem onClick={() => navigate('/shop?category=Dairy Products')}>
                    Dairy Products
                  </DropdownMenuItem>
                  <DropdownMenuItem onClick={() => navigate('/shop?category=Podulu')}>
                    Podulu
                  </DropdownMenuItem>
                  <DropdownMenuItem onClick={() => navigate('/shop?category=Papad')}>
                    Papad
                  </DropdownMenuItem>
                  <DropdownMenuItem onClick={() => navigate('/shop?category=Dehydrated Powders')}>
                    Dehydrated Powders
                  </DropdownMenuItem>
                </DropdownMenuContent>
              </DropdownMenu>
              <Link to="/about" className="text-gray-700 hover:text-orange-600 transition-colors font-medium">
                About us
              </Link>
            </nav>

            {/* Logo */}
            <Link to="/" className="flex items-center">
              <div className="w-16 h-16 bg-gradient-to-br from-orange-500 to-amber-500 rounded-full flex items-center justify-center shadow-lg">
                <span className="text-white font-bold text-xl">FW</span>
              </div>
            </Link>

            {/* Right Icons */}
            <div className="flex items-center space-x-4">
              {/* Search */}
              <form onSubmit={handleSearch} className="hidden md:flex items-center">
                <div className="relative">
                  <Input
                    type="text"
                    placeholder="Search products..."
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                    className="w-48 lg:w-64 pr-10"
                  />
                  <button type="submit" className="absolute right-3 top-1/2 -translate-y-1/2">
                    <Search size={18} className="text-gray-400" />
                  </button>
                </div>
              </form>

              {/* WhatsApp */}
              <a
                href="https://wa.me/918978152777"
                target="_blank"
                rel="noopener noreferrer"
                className="hidden sm:block text-gray-600 hover:text-green-600 transition-colors"
              >
                <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z" />
                </svg>
              </a>

              {/* User Menu */}
              <DropdownMenu>
                <DropdownMenuTrigger>
                  <User className="text-gray-600 hover:text-orange-600 transition-colors cursor-pointer" size={24} />
                </DropdownMenuTrigger>
                <DropdownMenuContent>
                  {user ? (
                    <>
                      <DropdownMenuItem onClick={() => navigate('/profile')}>
                        My Profile
                      </DropdownMenuItem>
                      <DropdownMenuItem onClick={() => navigate('/orders')}>
                        My Orders
                      </DropdownMenuItem>
                      <DropdownMenuItem onClick={handleLogout}>
                        Logout
                      </DropdownMenuItem>
                    </>
                  ) : (
                    <>
                      <DropdownMenuItem onClick={() => navigate('/login')}>
                        Login
                      </DropdownMenuItem>
                      <DropdownMenuItem onClick={() => navigate('/signup')}>
                        Sign Up
                      </DropdownMenuItem>
                    </>
                  )}
                </DropdownMenuContent>
              </DropdownMenu>

              {/* Wishlist */}
              <Link to="/wishlist" className="relative">
                <Heart className="text-gray-600 hover:text-orange-600 transition-colors" size={24} />
                {wishlistItems.length > 0 && (
                  <span className="absolute -top-2 -right-2 bg-orange-500 text-white text-xs rounded-full w-5 h-5 flex items-center justify-center">
                    {wishlistItems.length}
                  </span>
                )}
              </Link>

              {/* Cart */}
              <Link to="/cart" className="relative">
                <ShoppingCart className="text-gray-600 hover:text-orange-600 transition-colors" size={24} />
                {getCartCount() > 0 && (
                  <span className="absolute -top-2 -right-2 bg-orange-500 text-white text-xs rounded-full w-5 h-5 flex items-center justify-center">
                    {getCartCount()}
                  </span>
                )}
              </Link>
            </div>
          </div>
        </div>

        {/* Mobile Menu */}
        {mobileMenuOpen && (
          <div className="md:hidden border-t bg-white">
            <nav className="flex flex-col space-y-4 p-4">
              <Link to="/" className="text-gray-700 hover:text-orange-600" onClick={() => setMobileMenuOpen(false)}>
                Home
              </Link>
              <Link to="/shop" className="text-gray-700 hover:text-orange-600" onClick={() => setMobileMenuOpen(false)}>
                Shop
              </Link>
              <Link to="/about" className="text-gray-700 hover:text-orange-600" onClick={() => setMobileMenuOpen(false)}>
                About us
              </Link>
            </nav>
          </div>
        )}
      </header>

      <style jsx>{`
        @keyframes marquee {
          0% {
            transform: translateX(0);
          }
          100% {
            transform: translateX(-50%);
          }
        }
        .animate-marquee {
          display: inline-block;
          animation: marquee 20s linear infinite;
        }
      `}</style>
    </>
  );
};

export default Header;
