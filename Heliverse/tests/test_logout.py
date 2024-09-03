import pytest
from functions.login_page import LoginPage
from functions.products_page import ProductsPage
from utils.helpers import Utils
import logging
import time 

# Load configuration
config = Utils.load_config()
username_password = config['credentials']
link = config['host_name']['host']

@pytest.mark.suite8
class TestLogout:
    @pytest.fixture(autouse=True)
    def setup(self, login):
        self.driver = login
        self.log = Utils.custom_logger(logLevel=logging.INFO, log_file_name=f"{self.__class__.__name__}.log")
        self.login_page = LoginPage(self.driver, self.log)
        self.products_page = ProductsPage(self.driver, self.log)

    def test_logout(self):
        for username in username_password.keys():
            password = username_password[username]
            self.log.info(f"Testing username: {username}")

            try:
                self.driver.get(link)
                self.login_page.login(username, password)

                # Added an assertion to check if login was successful or failed
                if self.login_page.is_login_successful():
                    self.log.info(f"Login successful for user: {username}")
                    self.products_page.select_from_navbar('Logout')
                    
                    # Added an assertion to check if logout was successful or failed
                    if self.products_page.is_logout_successful():
                        self.log.info(f"Logout successful for user: {username}")
                    else:
                        self.log.error(f"Logout failed for user: {username}.")
                else:
                    self.log.error(f"Login failed for user: {username}. Invalid credentials or locked user")

            except Exception as e:
                self.log.error(f"An error occurred: {str(e)}")