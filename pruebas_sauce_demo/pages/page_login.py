from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page_Login():
    def __init__(self, driver):
        self.driver = driver
        self.user_name = (By.ID,'user-name')
        self.password = (By.ID,'password')
        self.login_button = (By.ID,'login-button')
    
    def login(self,usuario,password):
        # Espera hasta que el campo de nombre de usuario sea visible
        WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.user_name)
            )
        self.driver.find_element(*self.user_name).send_keys(usuario)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_button).click()