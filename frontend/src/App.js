import React from "react";
import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { CartProvider } from "./contexts/CartContext";
import { WishlistProvider } from "./contexts/WishlistContext";
import { AuthProvider } from "./contexts/AuthContext";
import { Toaster } from "./components/ui/toaster";

// Components
import Header from "./components/Header";
import Footer from "./components/Footer";

// Pages
import Home from "./pages/Home";
import Shop from "./pages/Shop";
import ProductDetail from "./pages/ProductDetail";
import Cart from "./pages/Cart";
import Wishlist from "./pages/Wishlist";
import Checkout from "./pages/Checkout";
import OrderSuccess from "./pages/OrderSuccess";
import Orders from "./pages/Orders";
import Profile from "./pages/Profile";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import About from "./pages/About";

// Admin Pages
import AdminLogin from "./pages/admin/AdminLogin";
import AdminDashboard from "./pages/admin/AdminDashboard";
import AdminProducts from "./pages/admin/AdminProducts";
import AdminOrders from "./pages/admin/AdminOrders";
import AdminSettings from "./pages/admin/AdminSettings";
import DownloadAndroid from "./pages/admin/DownloadAndroid";

function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <CartProvider>
          <WishlistProvider>
            <div className="App">
              <Routes>
                {/* Admin Routes (without Header/Footer) */}
                <Route path="/admin/login" element={<AdminLogin />} />
                <Route path="/admin/dashboard" element={<AdminDashboard />} />
                <Route path="/admin/products" element={<AdminProducts />} />
                <Route path="/admin/orders" element={<AdminOrders />} />
                <Route path="/admin/settings" element={<AdminSettings />} />
                <Route path="/admin/download-android" element={<DownloadAndroid />} />
                
                {/* Public Routes (with Header/Footer) */}
                <Route path="/" element={<><Header /><Home /><Footer /></>} />
                <Route path="/shop" element={<><Header /><Shop /><Footer /></>} />
                <Route path="/product/:id" element={<><Header /><ProductDetail /><Footer /></>} />
                <Route path="/cart" element={<><Header /><Cart /><Footer /></>} />
                <Route path="/wishlist" element={<><Header /><Wishlist /><Footer /></>} />
                <Route path="/checkout" element={<><Header /><Checkout /><Footer /></>} />
                <Route path="/order-success/:orderId" element={<><Header /><OrderSuccess /><Footer /></>} />
                <Route path="/orders" element={<><Header /><Orders /><Footer /></>} />
                <Route path="/profile" element={<><Header /><Profile /><Footer /></>} />
                <Route path="/login" element={<><Header /><Login /><Footer /></>} />
                <Route path="/signup" element={<><Header /><Signup /><Footer /></>} />
                <Route path="/about" element={<><Header /><About /><Footer /></>} />
              </Routes>
              <Toaster />
            </div>
          </WishlistProvider>
        </CartProvider>
      </AuthProvider>
    </BrowserRouter>
  );
}

export default App;
