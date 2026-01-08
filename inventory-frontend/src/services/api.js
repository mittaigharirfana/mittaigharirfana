import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8002/api';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Auth API
export const authAPI = {
  register: (username, email, password) => 
    api.post('/auth/register', null, { params: { username, email, password } }),
  login: (username, password) => 
    api.post('/auth/login', null, { params: { username, password } }),
};

// Products API
export const productsAPI = {
  getAll: () => api.get('/products'),
  getOne: (id) => api.get(`/products/${id}`),
  create: (data) => api.post('/products', data),
  update: (id, data) => api.put(`/products/${id}`, data),
  delete: (id) => api.delete(`/products/${id}`),
};

// Suppliers API
export const suppliersAPI = {
  getAll: () => api.get('/suppliers'),
  getOne: (id) => api.get(`/suppliers/${id}`),
  create: (data) => api.post('/suppliers', data),
  update: (id, data) => api.put(`/suppliers/${id}`, data),
  delete: (id) => api.delete(`/suppliers/${id}`),
};

// Purchases API
export const purchasesAPI = {
  getAll: () => api.get('/purchases'),
  getOne: (id) => api.get(`/purchases/${id}`),
  create: (data) => api.post('/purchases', data),
};

// Sales API
export const salesAPI = {
  getAll: () => api.get('/sales'),
  getOne: (id) => api.get(`/sales/${id}`),
  create: (data) => api.post('/sales', data),
};

// Alerts API
export const alertsAPI = {
  getAll: (resolved = null) => api.get('/alerts', { params: { resolved } }),
  resolve: (id) => api.put(`/alerts/${id}/resolve`),
};

// Reports API
export const reportsAPI = {
  getDashboard: () => api.get('/reports/dashboard'),
  getSalesReport: (startDate, endDate) => 
    api.get('/reports/sales', { params: { start_date: startDate, end_date: endDate } }),
  getPurchasesReport: (startDate, endDate) => 
    api.get('/reports/purchases', { params: { start_date: startDate, end_date: endDate } }),
  getStockValue: () => api.get('/reports/stock-value'),
};

export default api;
