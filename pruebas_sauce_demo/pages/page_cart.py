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
        self.remove_button_base = 'remove-'
        self.remove_shirt_id = 'remove-test.allthethings()-t-shirt-(red)'
        self.menu_burger_btn = (By.ID, 'react-burger-menu-btn')
        self.all_items_button = (By.ID, 'inventory_sidebar_link')
    
    def go_to_cart(self):
        self.driver.find_element(*self.cart).click()
    
    def get_cart_items(self):
        return [item.find_element(By.CLASS_NAME, 'inventory_item_name').text.strip().lower() for item in self.driver.find_elements(*self.cart_items_container)]
    
    
    def remove_element(self,element):
        try:
          pass
        except:
          print('An exception occurred')
    
    def remove_all_elements(self):
        try:
            # Encuentra todos los productos en el carrito
            cart_items = self.driver.find_elements(*self.cart_items_container)
        
            # Itera sobre cada producto y elimina
            for item in cart_items:
                product_name_element = item.find_element(By.CLASS_NAME, 'inventory_item_name')
                product_name = product_name_element.text.strip().lower()  # Extraer el nombre del producto
            
                # Identificar el botón de eliminar para cada producto dentro del `item` específico
                remove_button = item.find_element(By.XPATH, ".//button[contains(@id,'remove-')]")
            
                # Hacer clic en el botón para eliminar el producto
                remove_button.click()
                print(f"Producto '{product_name}' eliminado.")
            
        except NoSuchElementException as e:
            print(f"No se encontró el botón de eliminar para el producto . Error: {e}")
    
    def go_to_all_items(self):
        self.driver.find_element(*self.menu_burger_btn).click()
        # Espera explícita hasta que el botón esté presente
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.all_items_button)
        )
        # Después de la espera, haz clic en el botón
        burger_btn = self.driver.find_element(*self.all_items_button)
        burger_btn.click()
