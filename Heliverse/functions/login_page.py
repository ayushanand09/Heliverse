from selenium.webdriver.support import expected_conditions as EC
from locators.home_page_locators import HOMEPAGELocators
from locators.product_page_locators import PRODUCTPAGELocators
from functions.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver, log):
        super().__init__(driver, log)

    def load(self, link):
        self.driver.get(f'{link}')
        # self.driver.maximize_window()
        self.log.info("Loaded the url")
    
    def login(self, username, password):
        self.wait.until(EC.element_to_be_clickable(HOMEPAGELocators.USERNAME)).send_keys(username)
        self.wait.until(EC.element_to_be_clickable(HOMEPAGELocators.PASSWORD)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(HOMEPAGELocators.LOGIN_BUTTON)).click()

    def is_login_successful(self):
        try:
            # Wait for the success element to be present in the DOM
            self.wait.until(EC.presence_of_element_located(HOMEPAGELocators.SUCCESS_ELEMENT_FOR_LOGIN))
            return True
        except Exception as e:
            return False
        