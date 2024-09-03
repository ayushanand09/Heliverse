from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from locators.home_page_locators import HOMEPAGELocators
from locators.product_page_locators import PRODUCTPAGELocators
from locators.cart_page_locators import CARTPAGELocators
from locators.checkout_page_locators import CHECKOUTPAGELocators
from functions.base_page import BasePage
import time

class ProductsPage(BasePage):
    def __init__(self, driver, log):
        super().__init__(driver, log)
        self.counter = 0
    
    def load(self, link):
        self.driver.get(f'{link}')
        # self.driver.maximize_window()
        self.log.info("Loaded the url")
    
    def check_cart_badge(self):
        try:
            cart_counter = self.wait.until(EC.presence_of_element_located(PRODUCTPAGELocators.CART_BUTTON_VALUE))
            cart_value = int(cart_counter.text)
            return cart_value
        
        except NoSuchElementException:
            self.log.info("Cart badge <span> tag not found. Cart might be empty.")
            return 0
    
    def view_bike_light(self):
        product_selection = self.wait.until(EC.presence_of_element_located(PRODUCTPAGELocators.PRODUCT_BIKE_LIGHT))
        product_text = product_selection.text
        product_selection.click()
        return product_text
    
    def view_black_tshirt(self):
        product_selection = self.wait.until(EC.presence_of_element_located(PRODUCTPAGELocators.PRODUCT_TSHIRT_BLACK))
        product_text = product_selection.text
        product_selection.click()
        return product_text
    
    def view_onesie(self):
        product_selection = self.wait.until(EC.presence_of_element_located(PRODUCTPAGELocators.PRODUCT_ONESIE))
        product_text = product_selection.text
        product_selection.click()
        return product_text

    def view_red_tshirt(self):
        product_selection = self.wait.until(EC.presence_of_element_located(PRODUCTPAGELocators.PRODUCT_TSHIRT_RED))
        product_text = product_selection.text
        product_selection.click()
        return product_text
    
    def view_blackpack(self):
        product_selection = self.wait.until(EC.presence_of_element_located(PRODUCTPAGELocators.PRODUCT_BACKPACK))
        product_text = product_selection.text
        product_selection.click()
        return product_text
    
    def view_jacket(self):
        product_selection = self.wait.until(EC.presence_of_element_located(PRODUCTPAGELocators.PRODUCT_JACKET))
        product_text = product_selection.text
        product_selection.click()
        return product_text
    
    def view_product(self, txt):
        try:
            if txt == 'Bike Light':
                product_text = self.view_bike_light()
            elif txt == 'Black T-Shirt':
                product_text = self.view_black_tshirt()
            elif txt == 'Onesie':
                product_text = self.view_onesie()
            elif txt == 'Red T-Shirt':
                product_text = self.view_red_tshirt()
            elif txt == 'Backpack':
                product_text = self.view_blackpack()
            elif txt == 'Jacket':
                product_text = self.view_jacket()
            else:
                self.log.error(f"Product '{txt}' is not viewable in main page.")
            
            product_text_main = self.wait.until(EC.presence_of_element_located(PRODUCTPAGELocators.PRODUCT_NAME_MAIN_PAGE))
            product_text_main = product_text_main.text
            
            if product_text_main == product_text:
                self.log.info(f'Same product gets opened after clicking - {product_text_main}')
            else:
                self.log.error(f'Wrong product gets opened after clicking. Product clicked was {product_text} but {product_text_main} opened up.')
                
            back_home = self.wait.until(EC.presence_of_element_located(CHECKOUTPAGELocators.BACK_HOME_BTN))
            back_home.click()

        except Exception as e:
            self.log.error(f"str{e}")

    def select_bike_light(self):
        product_selection = self.wait.until(EC.presence_of_element_located(PRODUCTPAGELocators.PRODUCT_BIKE_LIGHT_ADD))
        product_selection.click()
    
    def select_black_tshirt(self):
        product_selection = self.wait.until(EC.presence_of_element_located(PRODUCTPAGELocators.PRODUCT_TSHIRT_BLACK_ADD))
        product_selection.click()
    
    def select_onesie(self):
        product_selection = self.wait.until(EC.presence_of_element_located(PRODUCTPAGELocators.PRODUCT_ONESIE_ADD))
        product_selection.click()

    def select_red_tshirt(self):
        product_selection = self.wait.until(EC.presence_of_element_located(PRODUCTPAGELocators.PRODUCT_TSHIRT_RED_ADD))
        product_selection.click()
    
    def select_blackpack(self):
        product_selection = self.wait.until(EC.presence_of_element_located(PRODUCTPAGELocators.PRODUCT_BACKPACK_ADD))
        product_selection.click()
    
    def select_jacket(self):
        product_selection = self.wait.until(EC.presence_of_element_located(PRODUCTPAGELocators.PRODUCT_JACKET_ADD))
        product_selection.click()
    
    def select_product(self, txt):
        try:
            if txt == 'Bike Light':
                self.select_bike_light()
            elif txt == 'Black T-Shirt':
                self.select_black_tshirt()
            elif txt == 'Onesie':
                self.select_onesie()
            elif txt == 'Red T-Shirt':
                self.select_red_tshirt()
            elif txt == 'Backpack':
                self.select_blackpack()
            elif txt == 'Jacket':
                self.select_jacket()
            else:
                self.log.error(f"Product '{txt}' is not recognized.")

            self.counter += 1
            cart_value = self.check_cart_badge()
            
            if self.counter == cart_value:
                self.log.info(f"Product '{txt}' was successfully clicked.")
            else:
                # If the cart value does not match the counter, decrement the counter
                self.counter -= 1
                self.log.error(f"Product '{txt}' is not clickable.")
            
        except Exception as e:
            self.log.error(f"Product '{txt}' is not clickable.")

    def open_navbar(self):
        hamburger_open = self.wait.until(EC.presence_of_element_located(PRODUCTPAGELocators.HAMBURGER))
        hamburger_open.click()
        self.log.info('Clicked on hamburger icon')

    def check_price(self):
        price = self.wait.until(EC.presence_of_element_located(PRODUCTPAGELocators.PRODUCT_PRICE_FP))
        price_value = price.text
        return price_value
    
    def select_from_navbar(self, txt):
        self.open_navbar()
        time.sleep(2)
        
        if txt == 'All Items':  
            price_before_click = self.check_price() 
            all_items = self.wait.until(EC.presence_of_element_located(PRODUCTPAGELocators.ALL_ITEMS))
            all_items.click()
            price_after_click = self.check_price()
            if(price_before_click == price_after_click):
                self.log.info('All Items functionality is working.')
            else:
                self.log.error('All Items functionality is working but the price of the products are changing dynamically on each click.')
        
        elif txt == 'Logout':
            logout = self.wait.until(EC.presence_of_element_located(PRODUCTPAGELocators.LOGOUT))
            logout.click()
            self.log.info('Clicked on Logout button functionality') 
        
        else:
            resest_state = self.wait.until(EC.presence_of_element_located(PRODUCTPAGELocators.RESET_APP_STATE))
            resest_state.click()
            self.log.info('Reset State functionality is working')
    
    def is_logout_successful(self):
        try:
            # Wait for the success element to be present in the DOM
            self.wait.until(EC.presence_of_element_located(HOMEPAGELocators.SUCCESS_ELEMENT_FOR_LOGOUT))
            return True
        except Exception as e:
            return False

    def close_navbar(self):
        hamburger_exit = self.wait.until(EC.presence_of_element_located(PRODUCTPAGELocators.EXIT_NAVBAR))
        hamburger_exit.click()
        self.log.info('Exited hamburger menu')

    def sort_Z_to_A(self, product_names):
        original_desc_sorted_names = sorted(product_names, reverse=True)
        
        sort_btn = self.wait.until(EC.presence_of_element_located(PRODUCTPAGELocators.SORT_BTN))
        sort_btn.click()
        sort_dropdown = Select(self.wait.until(EC.presence_of_element_located(PRODUCTPAGELocators.SORTING_OPTIONS)))
        sort_dropdown.select_by_value('za')
        time.sleep(2)

        website_product_names = self.wait.until(EC.presence_of_all_elements_located(PRODUCTPAGELocators.ALL_PRODCUTS_NAME))
        item_names = []
        for product_name in website_product_names:
            item_names.append(product_name.text)
        
        if original_desc_sorted_names == item_names:
            self.log.info('Sorting Z to A is working correctly')
        else:
            self.log.error('Sorting Z to A is not working correctly')
            self.log.info(f'expected_product_names -> {original_desc_sorted_names}')
            self.log.info(f'actual_product_names -> {item_names}')
    
    def sort_price_low_high(self, prices):
        original_prices = sorted(prices, key=float)

        sort_btn = self.wait.until(EC.presence_of_element_located(PRODUCTPAGELocators.SORT_BTN))
        sort_btn.click()
        sort_dropdown = Select(self.wait.until(EC.presence_of_element_located(PRODUCTPAGELocators.SORTING_OPTIONS)))
        sort_dropdown.select_by_value('lohi')
        time.sleep(2)

        website_prices = self.wait.until(EC.presence_of_all_elements_located(PRODUCTPAGELocators.ALL_PRICES))
        dollar_sign_item_prices = []
        for price in website_prices:
            dollar_sign_item_prices.append(price.text)
        item_prices = [price.replace('$', '') for price in dollar_sign_item_prices]
        
        if original_prices == item_prices:
            self.log.info('Sorting low to high is working correctly')
        else:
            self.log.error('Sorting low to high is not working correctly')
            self.log.info(f'expected_product_prices -> {original_prices}')
            self.log.info(f'actual_product_prices -> {item_prices}')
    
    def sort_price_high_low(self, prices):
        original_prices = sorted(prices, key=float, reverse=True)

        sort_btn = self.wait.until(EC.presence_of_element_located(PRODUCTPAGELocators.SORT_BTN))
        sort_btn.click()
        sort_dropdown = Select(self.wait.until(EC.presence_of_element_located(PRODUCTPAGELocators.SORTING_OPTIONS)))
        sort_dropdown.select_by_value('hilo')
        time.sleep(2)

        website_prices = self.wait.until(EC.presence_of_all_elements_located(PRODUCTPAGELocators.ALL_PRICES))
        dollar_sign_item_prices = []
        for price in website_prices:
            dollar_sign_item_prices.append(price.text)
        item_prices = [price.replace('$', '') for price in dollar_sign_item_prices]
        
        if original_prices == item_prices:
            self.log.info('Sorting high to low is working correctly')
        else:
            self.log.error('Sorting high to low is not working correctly')
            self.log.info(f'expected_product_prices -> {original_prices}')
            self.log.info(f'actual_product_prices -> {item_prices}')

    def sort_products(self, product_names, prices):
        self.sort_Z_to_A(product_names)
        self.sort_price_low_high(prices)
        self.sort_price_high_low(prices)

    def open_cart(self):
        cart_btn = self.wait.until(EC.presence_of_element_located(PRODUCTPAGELocators.CART_BUTTON))
        cart_btn.click()
        self.log.info('Opened Cart')