import React, { createContext, useContext, useState, useEffect } from 'react';

const AuthContext = createContext();

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within AuthProvider');
  }
  return context;
};

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  // Check for existing session on mount
  useEffect(() => {
    const savedUser = localStorage.getItem('freshwala_user');
    const token = localStorage.getItem('freshwala_token');
    
    if (savedUser && token) {
      setUser(JSON.parse(savedUser));
    }
    setLoading(false);
  }, []);

  const login = (userData, token) => {
    setUser(userData);
    localStorage.setItem('freshwala_user', JSON.stringify(userData));
    localStorage.setItem('freshwala_token', token);
  };

  const logout = () => {
    setUser(null);
    localStorage.removeItem('freshwala_user');
    localStorage.removeItem('freshwala_token');
    localStorage.removeItem('freshwala_cart');
    localStorage.removeItem('freshwala_wishlist');
  };

  const updateUser = (userData) => {
    setUser(userData);
    localStorage.setItem('freshwala_user', JSON.stringify(userData));
  };

  const isAuthenticated = () => {
    return !!user;
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        loading,
        login,
        logout,
        updateUser,
        isAuthenticated
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};
