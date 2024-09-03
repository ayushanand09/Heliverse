import pytest
import logging
from selenium import webdriver
from utils.helpers import Utils
from functions.login_page import LoginPage 
import os

# Load configuration
config = Utils.load_config()
username_password = config['credentials']
link = config['host_name']['host']

# Create necessary directories under Tests
base_test_dir = os.path.dirname(__file__)
report_folder_path = os.path.join(base_test_dir, 'Tests', 'Report')

# Ensure the report folder exists
if not os.path.exists(report_folder_path):
    os.makedirs(report_folder_path)

# driver initialization 
@pytest.fixture(scope="module")
def driver():
    # Setup
    driver = webdriver.Chrome()
    # Maximizing window
    driver.maximize_window()
    # Teardown
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def login(driver):
    # Create a logger for the login process
    log = Utils.custom_logger(logLevel=logging.INFO, log_file_name="PageLoad.log")
    login_page = LoginPage(driver, log)
    login_page.load(link)
    yield driver

def pytest_configure(config):
    # Get the current working directory
    cwd = os.getcwd()

    report_dir = os.path.join(cwd, 'Tests', 'Report')
    report_file = os.path.join(report_dir, 'report.html')

    # Set the report path in the pytest config
    config.option.htmlpath = report_file
