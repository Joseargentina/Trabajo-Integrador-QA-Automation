from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page_Cart():
    def __init__(self,driver) -> None:
        self.driver = driver
        self.cart = (By.ID, 'shopping_cart_container')
        self.cart_items_container = (By.CLASS_NAME, 'cart_item')
        self.remove_button = (By.ID, 'remove-sauce-labs')
        self.remove_shirt_id = 'remove-test.allthethings()-t-shirt-(red)'
        self.menu_burger_btn = (By.ID, 'react-burger-menu-btn')
        self.all_items_button = (By.ID, 'inventory_sidebar_link')
        self.xpath_remove = (By.XPATH, ".//button[contains(@id,'remove-')]")
        self.name_element = (By.CLASS_NAME, 'inventory_item_name')
        self.continue_shophing_btn = (By.ID, 'continue-shopping')
    
    def go_to_cart(self):
        self.driver.find_element(*self.cart).click()
    
    def get_cart_items(self):
        return [item.find_element(By.CLASS_NAME, 'inventory_item_name').text.strip().lower() for item in self.driver.find_elements(*self.cart_items_container)]
    
    
    def remove_element(self,element):
        try:
          items = self.driver.find_elements(*self.cart_items_container)
          for item in items:
              product_name_element = WebDriverWait(item, 10).until(
                    EC.visibility_of_element_located(self.name_element)
                ).text.strip().lower()
              if product_name_element == element.lower():
                  item.find_element(*self.xpath_remove).click()
                  print(f"Producto '{product_name_element}' eliminado.")
                  return
          print(f"Producto '{element}' no encontrado en el carrito.")
        except NoSuchElementException as e:
            print(f"No se encontró el botón de eliminar para el producto. Error: {e}")
    
    def remove_all_elements(self):
        try:
            cart_items = self.driver.find_elements(*self.cart_items_container)
        
            for item in cart_items:
                product_name_element = item.find_element(*self.name_element).text.strip().lower()
                remove_button = item.find_element(*self.xpath_remove)
            
                # Hacer clic en el botón para eliminar el producto
                remove_button.click()
                # print(f"Producto '{product_name_element}' eliminado.")
            
        except NoSuchElementException as e:
            print(f"No se encontró el botón de eliminar para el producto . Error: {e}")
    
    def go_to_all_items(self):
        self.driver.find_element(*self.menu_burger_btn).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.all_items_button)
        )
        self.driver.find_element(*self.all_items_button).click()
    
    def go_to_continue_shopping(self):
        self.driver.find_element(*self.continue_shophing_btn).click()
