from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page_Products():
    def __init__(self, driver):
      self.driver = driver
      self.dropdown = (By.CLASS_NAME, 'product_sort_container')
      self.price_elements = (By.CLASS_NAME, 'inventory_item_price')
      self.cart_items = (By.CLASS_NAME, 'cart_item')
    
    def sort_by_price_low_to_high(self, value):
        Select(self.driver.find_element(*self.dropdown)).select_by_value(value)
        
    def get_prices(self):
        items = self.driver.find_elements(*self.price_elements)
        prices = []
        for item in items:
            price_text = item.text
            try:
                price = float(price_text.replace('$', ''))
                prices.append(price)
            except ValueError:
                print(f"Error al convertir el precio: {price_text}")
        return prices
    
    def add_to_cart(self, element):
        try:
            # Construir el ID del botón basado en el nombre del producto
            element_id = 'add-to-cart-' + element.replace(' ', '-').lower()
            print(f"Buscando elemento con ID: {element_id}") 
            
        
            # Espera explícita hasta que el botón esté presente
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, element_id))
            )
            self.driver.find_element(By.ID, element_id).click()
        except NoSuchElementException as e:
            print(f"El producto '{element}' no se encontró.")
    
    def add_to_cart2(self,element):
        try:
          xpath= f'//button[contains(@id,"add-to-cart-{element.replace(' ','-').lower()}")]'
          print(f"Buscando elemento con XPath: {xpath}") 
          # Espera explícita hasta que el botón esté presente
          WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
          )
          
          self.driver.find_element(By.XPATH, xpath).click()
        except NoSuchElementException as e:
            print(f'No se encontro el elemento {element} a causa de: {e}')
          
    
    # def verify_cart_contents(self, product_to_add):
    #     cart_items = self.get_cart_items()
        
    #     for item in product_to_add:
    #         if item not in cart_items:
    #             print(f'El producto {item} no esta en el carrito')
    #             return False
    #     return True