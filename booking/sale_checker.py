#from selenium.webdriver.common.keys import Keys
from booking.send_email import SendEmail
import os
from selenium import webdriver

class Discount_manager(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers", teardown=False ):  
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Discount_manager, self).__init__(options=options) 
        self.implicitly_wait(15)
        self.maximize_window()

        

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()   


    def land_first_page(self, link):
        self.get(link)

    def agree_fn(self):
       agree_btn = self.find_element_by_id('sp-cc-accept')
       agree_btn.click()

    def price_check(self,wished_price):
        price_in_String = self.find_element_by_xpath('//*[@id="corePrice_feature_div"]/div/span/span[1]').get_attribute('innerHTML').strip()
        price_int = (float)(price_in_String.replace(price_in_String[0], ""))

        name_of_product = self.find_element_by_id('productTitle').get_attribute('innerHTML').strip()
        print(name_of_product)
        subject_email = f"sale found for {name_of_product} "
        message_email = f"sale found for {name_of_product} and the price was {price_int}"

        if(price_int <= wished_price):
            SendEmail.send_email(subject=subject_email ,message= message_email)
            print("sale found")
        else: print("No sale found for today")
        
        
            