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
        self.continue_button = (By.ID, 'continue')
        self.message_error = (By.XPATH, '//div[@class="error-message-container error"]/h3')
        self.menu_button = (By.ID,'react-burger-menu-btn')
        self.logout_btn = (By.ID, 'logout_sidebar_link')
        self.wait = WebDriverWait(self.driver, 10)
        
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
    
    def logout(self):
        # self.driver.find_element(*self.menu_button).click()
        # self.driver.find_element(*self.logout_btn).click()
        try:
            self.wait.until(EC.element_to_be_clickable(self.menu_button)).click()
            # Wait for the logout button to be visible and clickable
            logout_button = self.wait.until(EC.element_to_be_clickable(self.logout_btn))
            logout_button.click()
        except (NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error during logout: {e}")
        
