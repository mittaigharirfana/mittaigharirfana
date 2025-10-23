import React from 'react';
import { Link } from 'react-router-dom';
import { Facebook, Instagram, Twitter, Mail, Phone, MapPin } from 'lucide-react';

const Footer = () => {
  return (
    <footer className="bg-gray-900 text-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          {/* About */}
          <div>
            <h3 className="text-xl font-bold mb-4 text-orange-500">Freshwala</h3>
            <p className="text-gray-400 text-sm">
              Your one-stop destination for authentic homemade batters, pickles, and traditional spice powders.
            </p>
            <div className="flex space-x-4 mt-4">
              <a href="https://www.facebook.com/share/16NuCNAu5Y/?mibextid=wwXIfr" target="_blank" rel="noopener noreferrer" className="text-gray-400 hover:text-orange-500 transition-colors">
                <Facebook size={20} />
              </a>
              <a href="https://www.instagram.com/freshwalam?igsh=MXd6cWVodXl2d2JtbA%3D%3D&utm_source=qr" target="_blank" rel="noopener noreferrer" className="text-gray-400 hover:text-orange-500 transition-colors">
                <Instagram size={20} />
              </a>
            </div>
          </div>

          {/* Quick Links */}
          <div>
            <h3 className="text-lg font-semibold mb-4">Quick Links</h3>
            <ul className="space-y-2">
              <li>
                <Link to="/" className="text-gray-400 hover:text-orange-500 transition-colors text-sm">
                  Home
                </Link>
              </li>
              <li>
                <Link to="/shop" className="text-gray-400 hover:text-orange-500 transition-colors text-sm">
                  Shop
                </Link>
              </li>
              <li>
                <Link to="/about" className="text-gray-400 hover:text-orange-500 transition-colors text-sm">
                  About Us
                </Link>
              </li>
              <li>
                <Link to="/contact" className="text-gray-400 hover:text-orange-500 transition-colors text-sm">
                  Contact
                </Link>
              </li>
            </ul>
          </div>

          {/* Categories */}
          <div>
            <h3 className="text-lg font-semibold mb-4">Categories</h3>
            <ul className="space-y-2">
              <li>
                <Link to="/shop?category=Pickles" className="text-gray-400 hover:text-orange-500 transition-colors text-sm">
                  Pickles
                </Link>
              </li>
              <li>
                <Link to="/shop?category=Batters" className="text-gray-400 hover:text-orange-500 transition-colors text-sm">
                  Batters
                </Link>
              </li>
              <li>
                <Link to="/shop?category=Dairy Products" className="text-gray-400 hover:text-orange-500 transition-colors text-sm">
                  Dairy Products
                </Link>
              </li>
              <li>
                <Link to="/shop?category=Podulu" className="text-gray-400 hover:text-orange-500 transition-colors text-sm">
                  Podulu
                </Link>
              </li>
            </ul>
          </div>

          {/* Contact Info */}
          <div>
            <h3 className="text-lg font-semibold mb-4">Contact Us</h3>
            <ul className="space-y-3">
              <li className="flex items-start space-x-2 text-sm text-gray-400">
                <MapPin size={18} className="text-orange-500 mt-1 flex-shrink-0" />
                <span>Hyderabad, Telangana, India</span>
              </li>
              <li className="flex items-center space-x-2 text-sm text-gray-400">
                <Phone size={18} className="text-orange-500 flex-shrink-0" />
                <span>+91 98765 43210</span>
              </li>
              <li className="flex items-center space-x-2 text-sm text-gray-400">
                <Mail size={18} className="text-orange-500 flex-shrink-0" />
                <span>info@freshwala.com</span>
              </li>
            </ul>
          </div>
        </div>

        <div className="border-t border-gray-800 mt-8 pt-8 text-center">
          <p className="text-gray-400 text-sm">
            © {new Date().getFullYear()} Freshwala. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
