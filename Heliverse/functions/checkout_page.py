# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from locators.cart_page_locators import CARTPAGELocators
from locators.checkout_page_locators import CHECKOUTPAGELocators
from functions.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, driver, log):
        super().__init__(driver, log)
    
    def remove_backpack(self):
        remove_backpack = self.wait.until(EC.presence_of_element_located(CARTPAGELocators.PRODUCT_REMOVE_BACKPACK))
        remove_backpack.click()
        self.log.info('Removed Backpack from cart')
    
    def remove_bike_light(self):
        remove_bike_light = self.wait.until(EC.presence_of_element_located(CARTPAGELocators.PRODUCT_REMOVE_BIKE_LIGHT))
        remove_bike_light.click()
        self.log.info('Removed Bike Light from cart')
    
    def remove_black_tshirt(self):
        remove_black_tshirt = self.wait.until(EC.presence_of_element_located(CARTPAGELocators.PRODUCT_REMOVE_TSHIRT_BLACK))
        remove_black_tshirt.click()
        self.log.info('Removed Black T-Shirt from cart')
    
    def remove_jacket(self):
        remove_jacket = self.wait.until(EC.presence_of_element_located(CARTPAGELocators.PRODUCT_REMOVE_JACKET))
        remove_jacket.click()
        self.log.info('Removed Jacket from cart')
    
    def remove_red_tshirt(self):
        remove_red_tshirt = self.wait.until(EC.presence_of_element_located(CARTPAGELocators.PRODUCT_REMOVE_TSHIRT_RED))
        remove_red_tshirt.click()
        self.log.info('Removed Red T-Shirt from cart')
    
    def remove_onesie(self):
        remove_onesie = self.wait.until(EC.presence_of_element_located(CARTPAGELocators.PRODUCT_REMOVE_ONESIE))
        remove_onesie.click()

    def remove_from_cart(self, txt):
        if txt == "Bike Light":
            self.remove_bike_light()
        elif txt == "Black T-Shirt":
            self.remove_black_tshirt()
        elif txt == "Onesie":
            self.remove_onesie()
        elif txt == "Red T-Shirt":
            self.remove_red_tshirt()
        elif txt == "Backpack":
            self.remove_backpack()
        else:
            self.remove_jacket()

    def continue_shopping(self):
        continue_btn = self.wait.until(EC.presence_of_element_located(CARTPAGELocators.CONTINUE_SHOPPING))
        continue_btn.click()

    def checkout(self):
        checkout_btn = self.wait.until(EC.presence_of_element_located(CARTPAGELocators.CHECKOUT))
        checkout_btn.click() 

    def enter_first_name(self, text):
        first_name = self.wait.until(EC.presence_of_element_located(CHECKOUTPAGELocators.FIRST_NAME))
        first_name.clear()
        first_name.send_keys(text)

        entered_first_name = first_name.get_attribute("value")
        if entered_first_name:
            self.log.info('First name data successfully entered')
        else:
            self.log.error('First name data not entered')

    def enter_last_name(self,text):
        first_name = self.wait.until(EC.presence_of_element_located(CHECKOUTPAGELocators.FIRST_NAME))
        last_name = self.wait.until(EC.presence_of_element_located(CHECKOUTPAGELocators.LAST_NAME))
        
        original_first_name = first_name.get_attribute("value")
        last_name.clear()
        last_name.send_keys(text)
        entered_last_name = last_name.get_attribute("value")
        new_first_name = first_name.get_attribute("value")
        
        if entered_last_name:
            self.log.info('Last name data successfully entered')
        else:
            if original_first_name == new_first_name:
                self.log.error('Last name data not entered and it has not replaced the data present in first name field.')
            else:
                self.log.error('Last name data not entered and it has replaced the data present in first name field.')

    def enter_zipcode(self,text):
        zipcode = self.wait.until(EC.presence_of_element_located(CHECKOUTPAGELocators.ZIPCODE))
        zipcode.clear()
        zipcode.send_keys(text)

        entered_zipcode = zipcode.get_attribute("value")
        if entered_zipcode:
            self.log.info('Zipcode data successfully entered')
        else:
            self.log.error('Zipcode data not entered')
    
    def check_final_details(self):
        success_text_1 = 'Checkout: Overview'
        success_text_2 = 'Checkout: Complete!'
        
        first_name = self.wait.until(EC.presence_of_element_located(CHECKOUTPAGELocators.FIRST_NAME))
        last_name = self.wait.until(EC.presence_of_element_located(CHECKOUTPAGELocators.LAST_NAME))
        zipcode = self.wait.until(EC.presence_of_element_located(CHECKOUTPAGELocators.ZIPCODE))

        entered_first_name = first_name.get_attribute("value")
        entered_last_name = last_name.get_attribute("value")
        entered_zipcode = zipcode.get_attribute("value")

        if entered_first_name and entered_last_name and entered_zipcode and success_text_1 == self.continue_from_checkout():
            self.log.info('Entire checkout functionality is correct.')
        else:
            if self.continue_from_checkout() == success_text_1:
                self.log.error('Continue button is executable even after the input fields are empty.')
                if self.finish_from_checkout() != success_text_2 :
                    self.log.error('Finish button is not clickable. Although, it should not be clicked as well because the input fields were previously empty.')
                else:
                    self.log.error('Finish button is clickable but since the input fields were empty this page should not have appeared.')
            else:
                self.log.error('Continue button is not executable.')

    def enter_personal_details(self, fname, lname, zip):
        self.checkout()
        self.enter_first_name(fname)
        self.enter_last_name(lname)
        self.enter_zipcode(zip)
        self.check_final_details()

    def cancel_from_checkout(self):
        cancel_btn = self.wait.until(EC.presence_of_element_located(CHECKOUTPAGELocators.CANCEL_BTN))
        cancel_btn.click()
    
    def continue_from_checkout(self):
        continue_btn = self.wait.until(EC.presence_of_element_located(CHECKOUTPAGELocators.CONTINUE_BTN))
        continue_btn.click()
        try:
            # Wait for the success element to be present in the DOM
            success_txt = self.wait.until(EC.presence_of_element_located(CHECKOUTPAGELocators.SUCCESS_ELEMENT_CHECKOUT))
            success_txt = success_txt.text
            return success_txt
        except Exception as e:
            return "Error"

    def finish_from_checkout(self):
        finish_btn = self.wait.until(EC.presence_of_element_located(CHECKOUTPAGELocators.FINISH_BTN))
        finish_btn.click()
        try:
            # Wait for the success element to be present in the DOM
            success_txt = self.wait.until(EC.presence_of_element_located(CHECKOUTPAGELocators.SUCCESS_ELEMENT_CHECKOUT))
            success_txt = success_txt.text
            return success_txt
        except Exception as e:
            return "Error"
        
    def back_to_products_page(self):
        back_home_btn = self.wait.until(EC.presence_of_element_located(CHECKOUTPAGELocators.BACK_HOME_BTN))
        back_home_btn.click()
        self.log.info('Successfully navigated back to home page.')