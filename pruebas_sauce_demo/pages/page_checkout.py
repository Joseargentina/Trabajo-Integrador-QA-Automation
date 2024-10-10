from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

class Page_Checkout():
    def __init__(self, driver):
        self.driver = driver
        self.checkout = (By.ID, 'checkout')
        self.first_name = (By.ID, 'first-name')
        self.last_name = (By.ID, 'last-name')
        self.postal_code = (By.ID, 'postal-code')
        self.continue_button = (By.ID, 'continue')
        self.message_error = (By.XPATH, '//div[@class="error-message-container error"]/h3')
        self.menu_button = (By.ID,'react-burger-menu-btn')
        self.logout_btn = (By.ID, 'logout_sidebar_link')
        self.wait = WebDriverWait(self.driver, 10)
        self.finish_button = (By.ID, 'finish')
        self.message_final = (By.XPATH, '//h2[contains(@class, "complete-header")]')
        
    def go_to_checkout(self):
        self.driver.find_element(*self.checkout).click() 
    
    def insert_first_name(self,value):
        self.driver.find_element(*self.first_name).send_keys(value)
    
    def insert_last_name(self,value):
        self.driver.find_element(*self.last_name).send_keys(value)
    
    def go_to_continue(self):
        self.driver.find_element(*self.continue_button).click()  
    
    def get_message_error(self):
        return self.driver.find_element(*self.message_error).text
    
    def fill_checkout(self,first_name,last_name,num_postal_code):
        try:
          if isinstance(first_name, str) and isinstance(last_name,str) and isinstance(num_postal_code,(int,float)):
            self.driver.find_element(*self.first_name).send_keys(first_name)
            self.driver.find_element(*self.last_name).send_keys(last_name)
            self.driver.find_element(*self.postal_code).send_keys(num_postal_code)
          else:
            print("Los parámetros proporcionados son inválidos.")
        except NoSuchElementException:
          print("No se encontró uno de los elementos necesarios para llenar el formulario.")
    
    def finish_buy(self):
        self.driver.find_element(*self.finish_button).click()
    
    def get_message_final(self):
        try:
            message_element = self.wait.until(
                EC.visibility_of_element_located(self.message_final)
            )
            return message_element.text
        except NoSuchElementException:
            return "El mensaje final no se encontró."
          
        
        
