# product_page_locators 
from selenium.webdriver.common.by import By

class PRODUCTPAGELocators:

    # Navbar
    HAMBURGER = (By.XPATH, '//*[@id="react-burger-menu-btn"]')
    ALL_ITEMS = (By.XPATH, '//*[@id="inventory_sidebar_link"]')
    LOGOUT = (By.XPATH, '//*[@id="logout_sidebar_link"]')
    RESET_APP_STATE = (By.XPATH, '//*[@id="reset_sidebar_link"]')
    EXIT_NAVBAR = (By.XPATH , '//*[@id="react-burger-cross-btn"]')

    # Main Page
    PRODUCT_BIKE_LIGHT = (By.XPATH, '//*[@id="item_0_title_link"]/div')
    PRODUCT_BIKE_LIGHT_ADD = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')

    PRODUCT_TSHIRT_BLACK = (By.XPATH, '//*[@id="item_1_title_link"]/div')
    PRODUCT_TSHIRT_BLACK_ADD = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')

    PRODUCT_ONESIE = (By.XPATH, '//*[@id="item_2_title_link"]/div')
    PRODUCT_ONESIE_ADD = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]')

    PRODUCT_TSHIRT_RED = (By.XPATH, '//*[@id="item_3_title_link"]/div')
    PRODUCT_TSHIRT_RED_ADD = (By.XPATH, '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
    
    PRODUCT_BACKPACK = (By.XPATH, '//*[@id="item_4_title_link"]/div')
    PRODUCT_BACKPACK_ADD = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    
    PRODUCT_JACKET = (By.XPATH, '//*[@id="item_5_title_link"]/div')
    PRODUCT_JACKET_ADD = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')

    PRODUCT_NAME_MAIN_PAGE = (By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[1]')
    PRODUCT_PRICE_FP = (By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
    
    # ALL_PRODCUTS_NAME = (By.XPATH, '//*[@id="inventory_container"]/div')
    ALL_PRODCUTS_NAME = (By.CSS_SELECTOR, "div[data-test='inventory-item-name']")
    ALL_PRICES = (By.CSS_SELECTOR, "div[data-test='inventory-item-price']")
    # Sorting Menu
    SORT_BTN = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span')
    SORTING_OPTIONS = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select')

    # Cart Button
    CART_BUTTON = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
    CART_BUTTON_VALUE = (By.XPATH, '//*[@id="shopping_cart_container"]/a/span')