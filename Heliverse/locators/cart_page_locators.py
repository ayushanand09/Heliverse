# cart_page_locators.py

from selenium.webdriver.common.by import By

class CARTPAGELocators:
    
    PRODUCT_REMOVE_BACKPACK = (By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')
    PRODUCT_REMOVE_BIKE_LIGHT = (By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]')
    PRODUCT_REMOVE_TSHIRT_BLACK = (By.XPATH, '//*[@id="remove-sauce-labs-bolt-t-shirt"]')
    PRODUCT_REMOVE_JACKET = (By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]')
    PRODUCT_REMOVE_TSHIRT_RED = (By.XPATH, '//*[@id="remove-test.allthethings()-t-shirt-(red)"]')
    PRODUCT_REMOVE_ONESIE = (By.XPATH, '//*[@id="remove-sauce-labs-onesie"]')

    CONTINUE_SHOPPING = (By.XPATH, '//*[@id="continue-shopping"]')
    CHECKOUT = (By.XPATH, '//*[@id="checkout"]')
