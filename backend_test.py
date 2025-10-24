#!/usr/bin/env python3
"""
Freshwala Backend API Testing Suite
Tests all backend APIs for the Freshwala e-commerce platform
"""

import requests
import json
import sys
from datetime import datetime

# Backend URL from frontend .env
BASE_URL = "https://grocery-express-19.preview.emergentagent.com/api"

class FreshwalaAPITester:
    def __init__(self):
        self.base_url = BASE_URL
        self.test_results = []
        self.failed_tests = []
        
    def log_test(self, test_name, success, message, response_data=None):
        """Log test results"""
        result = {
            'test': test_name,
            'success': success,
            'message': message,
            'timestamp': datetime.now().isoformat(),
            'response_data': response_data
        }
        self.test_results.append(result)
        
        if not success:
            self.failed_tests.append(result)
            
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {test_name}: {message}")
        
    def test_api_root(self):
        """Test the root API endpoint"""
        try:
            response = requests.get(f"{self.base_url}/")
            if response.status_code == 200:
                data = response.json()
                if "message" in data and "Freshwala API" in data["message"]:
                    self.log_test("API Root", True, "API is running correctly")
                    return True
                else:
                    self.log_test("API Root", False, f"Unexpected response: {data}")
                    return False
            else:
                self.log_test("API Root", False, f"Status code: {response.status_code}")
                return False
        except Exception as e:
            self.log_test("API Root", False, f"Connection error: {str(e)}")
            return False
    
    def test_get_all_products(self):
        """Test GET /api/products - Should return all 12 products"""
        try:
            response = requests.get(f"{self.base_url}/products")
            if response.status_code == 200:
                products = response.json()
                if isinstance(products, list):
                    if len(products) == 12:
                        self.log_test("Get All Products", True, f"Retrieved {len(products)} products as expected", products[:2])
                        return True
                    else:
                        self.log_test("Get All Products", False, f"Expected 12 products, got {len(products)}")
                        return False
                else:
                    self.log_test("Get All Products", False, f"Expected list, got {type(products)}")
                    return False
            else:
                self.log_test("Get All Products", False, f"Status code: {response.status_code}")
                return False
        except Exception as e:
            self.log_test("Get All Products", False, f"Error: {str(e)}")
            return False
    
    def test_get_single_product(self):
        """Test GET /api/products/1 - Should return Avakaya Pickle product details"""
        try:
            response = requests.get(f"{self.base_url}/products/1")
            if response.status_code == 200:
                product = response.json()
                if isinstance(product, dict):
                    if product.get('name') == 'Avakaya Pickle' and product.get('id') == '1':
                        self.log_test("Get Single Product", True, f"Retrieved product: {product['name']}", product)
                        return True
                    else:
                        self.log_test("Get Single Product", False, f"Expected Avakaya Pickle with id=1, got {product.get('name')} with id={product.get('id')}")
                        return False
                else:
                    self.log_test("Get Single Product", False, f"Expected dict, got {type(product)}")
                    return False
            else:
                self.log_test("Get Single Product", False, f"Status code: {response.status_code}")
                return False
        except Exception as e:
            self.log_test("Get Single Product", False, f"Error: {str(e)}")
            return False
    
    def test_get_products_by_category(self):
        """Test GET /api/products?category=Pickles - Should return only pickle products"""
        try:
            response = requests.get(f"{self.base_url}/products?category=Pickles")
            if response.status_code == 200:
                products = response.json()
                if isinstance(products, list):
                    pickle_products = [p for p in products if p.get('category') == 'Pickles']
                    if len(pickle_products) == len(products) and len(products) > 0:
                        expected_pickles = ['Avakaya Pickle', 'Gongura Pickle', 'Tomato Pickle']
                        found_pickles = [p['name'] for p in products]
                        if all(name in found_pickles for name in expected_pickles):
                            self.log_test("Get Products by Category", True, f"Retrieved {len(products)} pickle products", products)
                            return True
                        else:
                            self.log_test("Get Products by Category", False, f"Missing expected pickles. Found: {found_pickles}")
                            return False
                    else:
                        self.log_test("Get Products by Category", False, f"Expected only pickle products, got mixed categories")
                        return False
                else:
                    self.log_test("Get Products by Category", False, f"Expected list, got {type(products)}")
                    return False
            else:
                self.log_test("Get Products by Category", False, f"Status code: {response.status_code}")
                return False
        except Exception as e:
            self.log_test("Get Products by Category", False, f"Error: {str(e)}")
            return False
    
    def test_get_categories(self):
        """Test GET /api/categories - Should return 6 categories"""
        try:
            response = requests.get(f"{self.base_url}/categories")
            if response.status_code == 200:
                categories = response.json()
                if isinstance(categories, list):
                    if len(categories) == 6:
                        expected_categories = ['Podulu', 'Dehydrated Powders', 'Dairy Products', 'Papad', 'Pickles', 'Batters']
                        found_categories = [c['name'] for c in categories]
                        if all(name in found_categories for name in expected_categories):
                            self.log_test("Get Categories", True, f"Retrieved all {len(categories)} expected categories", categories)
                            return True
                        else:
                            missing = [name for name in expected_categories if name not in found_categories]
                            self.log_test("Get Categories", False, f"Missing categories: {missing}")
                            return False
                    else:
                        self.log_test("Get Categories", False, f"Expected 6 categories, got {len(categories)}")
                        return False
                else:
                    self.log_test("Get Categories", False, f"Expected list, got {type(categories)}")
                    return False
            else:
                self.log_test("Get Categories", False, f"Status code: {response.status_code}")
                return False
        except Exception as e:
            self.log_test("Get Categories", False, f"Error: {str(e)}")
            return False
    
    def test_create_order(self):
        """Test POST /api/orders/create with sample order data"""
        order_data = {
            "amount": 50000,  # 500 rupees in paise
            "items": [
                {
                    "productId": "1",
                    "name": "Avakaya Pickle",
                    "quantity": 2,
                    "price": 250
                }
            ],
            "shippingAddress": {
                "name": "Rajesh Kumar",
                "phone": "9876543210",
                "address": "123 MG Road, Banjara Hills",
                "city": "Hyderabad",
                "state": "Telangana",
                "pincode": "500034"
            }
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/orders/create",
                json=order_data,
                headers={'Content-Type': 'application/json'}
            )
            
            if response.status_code == 200:
                result = response.json()
                if 'orderId' in result and 'razorpayOrderId' in result:
                    # Store order ID for later tests
                    self.created_order_id = result['orderId']
                    self.log_test("Create Order", True, f"Order created successfully. OrderID: {result['orderId']}", result)
                    return True
                else:
                    self.log_test("Create Order", False, f"Missing orderId or razorpayOrderId in response: {result}")
                    return False
            else:
                error_msg = f"Status code: {response.status_code}"
                try:
                    error_detail = response.json()
                    error_msg += f", Error: {error_detail}"
                except:
                    error_msg += f", Response: {response.text}"
                self.log_test("Create Order", False, error_msg)
                return False
        except Exception as e:
            self.log_test("Create Order", False, f"Error: {str(e)}")
            return False
    
    def test_get_orders(self):
        """Test GET /api/orders - Should return the created order"""
        try:
            response = requests.get(f"{self.base_url}/orders")
            if response.status_code == 200:
                orders = response.json()
                if isinstance(orders, list):
                    if len(orders) > 0:
                        # Check if our created order exists (if we have the order ID)
                        if hasattr(self, 'created_order_id'):
                            found_order = next((o for o in orders if o.get('orderId') == self.created_order_id), None)
                            if found_order:
                                self.log_test("Get Orders", True, f"Retrieved {len(orders)} orders including our created order", orders[:1])
                                return True
                            else:
                                self.log_test("Get Orders", False, f"Created order {self.created_order_id} not found in orders list")
                                return False
                        else:
                            self.log_test("Get Orders", True, f"Retrieved {len(orders)} orders (no specific order to verify)", orders[:1])
                            return True
                    else:
                        self.log_test("Get Orders", False, "No orders found")
                        return False
                else:
                    self.log_test("Get Orders", False, f"Expected list, got {type(orders)}")
                    return False
            else:
                self.log_test("Get Orders", False, f"Status code: {response.status_code}")
                return False
        except Exception as e:
            self.log_test("Get Orders", False, f"Error: {str(e)}")
            return False
    
    def run_all_tests(self):
        """Run all API tests"""
        print(f"🚀 Starting Freshwala Backend API Tests")
        print(f"📍 Testing against: {self.base_url}")
        print("=" * 60)
        
        # Test API connectivity first
        if not self.test_api_root():
            print("❌ API is not accessible. Stopping tests.")
            return False
        
        # Run all tests
        tests = [
            self.test_get_all_products,
            self.test_get_single_product,
            self.test_get_products_by_category,
            self.test_get_categories,
            self.test_create_order,
            self.test_get_orders
        ]
        
        for test in tests:
            test()
            print()  # Add spacing between tests
        
        # Summary
        print("=" * 60)
        print("📊 TEST SUMMARY")
        print("=" * 60)
        
        total_tests = len(self.test_results)
        passed_tests = len([t for t in self.test_results if t['success']])
        failed_tests = len(self.failed_tests)
        
        print(f"Total Tests: {total_tests}")
        print(f"✅ Passed: {passed_tests}")
        print(f"❌ Failed: {failed_tests}")
        print(f"Success Rate: {(passed_tests/total_tests)*100:.1f}%")
        
        if self.failed_tests:
            print("\n🔍 FAILED TESTS DETAILS:")
            print("-" * 40)
            for test in self.failed_tests:
                print(f"❌ {test['test']}: {test['message']}")
        
        return failed_tests == 0

if __name__ == "__main__":
    tester = FreshwalaAPITester()
    success = tester.run_all_tests()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)