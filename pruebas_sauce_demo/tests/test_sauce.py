import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from dotenv import load_dotenv
import os
from selenium.webdriver.common.by import By
from pages.page_login import Page_Login
from pages.page_products import Page_Products
from pages.page_checkout import Page_Checkout
from pages.page_cart import Page_Cart

class Sauce_demo_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        options = Options()
        options.add_argument('--incognito')
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        cls.driver = webdriver.Firefox(options=options)
        load_dotenv()
        cls.base_url = os.getenv('BASE_URL')
        cls.user = os.getenv('NAME_USER')
        cls.password = os.getenv('PASSWORD')
        print(f"Base URL: {cls.base_url}")
        # print(f"Base URL: {cls.base_url}, User: {cls.user}, Password: {cls.password}")

    @classmethod
    def tearDownClass(cls) -> None:        
        cls.driver.close()
        cls.driver.quit()     

    def setUp(self) -> None:
        self.driver.implicitly_wait(10)
        self.driver.get(self.base_url) 
        self.page_login = Page_Login(self.driver)
        self.page_login.login(self.user, self.password)
        self.page_products = Page_Products(self.driver)
        self.page_checkout = Page_Checkout(self.driver)
        self.page_cart= Page_Cart(self.driver) 
        
    def tearDown(self) -> None:
        self.driver.delete_all_cookies()
    
    def test_order_by_price_and_verify(self):
        self.page_products.sort_by_price_low_to_high('lohi')
        prices = self.page_products.get_prices()
        self.assertEqual(prices, sorted(prices))
    
    def test_checkout_errors_after_adding_all_items(self):
        products_to_add= [
            'sauce labs backpack',
            'sauce labs bike light',
            'sauce labs bolt t-shirt',
            'sauce labs fleece jacket',
            'sauce labs onesie',
            'test.allthethings() T-shirt (red)'
        ]
        for product in products_to_add:
            self.page_products.add_to_cart2(product)
            
        self.page_cart.go_to_cart()
        cart_items = self.page_cart.get_cart_items()
       
        normalized_products = [item.strip().lower() for item in products_to_add]
       
        self.assertCountEqual( cart_items, normalized_products)
        
        self.page_checkout.go_to_checkout()
        
        self.page_checkout.insert_first_name('andres')
        self.page_checkout.go_to_continue()
        self.assertEqual('Error: Last Name is required', self.page_checkout.get_message_error())
        
        self.page_checkout.insert_last_name('Saldias')
        self.page_checkout.go_to_continue()
        self.assertEqual('Error: Postal Code is required', self.page_checkout.get_message_error())
        

    def test_standard_user_complete_checkout_process(self):
        self.page_cart.go_to_cart()
        if self.page_cart.get_cart_items():
            self.page_cart.remove_all_elements()
        
        self.page_cart.go_to_all_items()
        self.page_products.add_to_cart2('sauce labs onesie')
        self.page_cart.go_to_cart()
        self.page_cart.remove_element('sauce labs onesie')
        self.assertEqual(len(self.page_cart.get_cart_items()),0 ,'El carrito debería estar vacío')
        self.page_cart.go_to_continue_shopping()
        products_to_add = ['sauce labs bolt t-shirt','sauce labs fleece jacket']
        for product in products_to_add:
            self.page_products.add_to_cart2(product)
        
        self.page_cart.go_to_cart()
        cart_items = self.page_cart.get_cart_items()
        self.assertEqual(cart_items,products_to_add,'El carrito debería estar vacío después de eliminar el artículo.')
        self.page_checkout.go_to_checkout()
        self.page_checkout.fill_checkout('Jose','Perez',6534)
        self.page_checkout.go_to_continue()
        self.page_checkout.finish_buy()
        message =self.page_checkout.get_message_final()
        self.assertEqual('Thank you for your order!', message, 'El mensaje final no es el esperado.')
    
if __name__ == '__main__':
    unittest.main()
