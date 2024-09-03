# home_page_locators.py
from selenium.webdriver.common.by import By

class HOMEPAGELocators:

    # Home Page 
    USERNAME = (By.XPATH, '//*[@id="user-name"]')
    PASSWORD = (By.XPATH, '//*[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login-button"]')
    SUCCESS_ELEMENT_FOR_LOGIN = (By.XPATH, '//*[@id="header_container"]/div[2]/span')
    SUCCESS_ELEMENT_FOR_LOGOUT = (By.XPATH, '//*[@id="user-name"]')