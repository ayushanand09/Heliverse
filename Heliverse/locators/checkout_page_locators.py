# checkout_page_locators.py

from selenium.webdriver.common.by import By

class CHECKOUTPAGELocators:
    FIRST_NAME = (By.XPATH, '//*[@id="first-name"]')
    LAST_NAME = (By.XPATH, '//*[@id="last-name"]')
    ZIPCODE =  (By.XPATH, '//*[@id="postal-code"]')

    CANCEL_BTN = (By.XPATH, '//*[@id="cancel"]')
    CONTINUE_BTN = (By.XPATH, '//*[@id="continue"]')
    FINISH_BTN = (By.XPATH, '//*[@id="finish"]')
    BACK_HOME_BTN = (By.XPATH, '//*[@id="back-to-products"]')

    SUCCESS_ELEMENT_CHECKOUT = (By.XPATH, '//*[@id="header_container"]/div[2]/span')