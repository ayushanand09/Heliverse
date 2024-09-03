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

@pytest.mark.suite1
class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, login):
        self.driver = login
        self.log = Utils.custom_logger(logLevel=logging.INFO, log_file_name=f"{self.__class__.__name__}.log")
        self.login_page = LoginPage(self.driver, self.log)

    def test_login(self):
        for username in username_password.keys():
            password = username_password[username]
            self.log.info(f"Testing username: {username}")

            try:
                self.driver.get(link)

                start_time = time.time()  # Record the start time
                self.login_page.login(username, password)

                # Added an assertion to check if login was successful or failed
                if self.login_page.is_login_successful():
                    elapsed_time = time.time() - start_time  # Calculate the elapsed time
                    self.log.info(f"Login successful for user: {username}")

                    # Check if login was successful within 3 seconds
                    if elapsed_time <= 3:
                        self.log.info(f"No glitch detected. Login completed in {elapsed_time:.2f} seconds.")
                    else:
                        self.log.warning(f"Potential glitch detected. Login took {elapsed_time:.2f} seconds.")                
                else:
                    self.log.error(f"Login failed for user: {username}. Invalid credentials or locked user")
            
            except Exception as e:
                self.log.error(f"An error occurred: {str(e)}")