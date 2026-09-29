from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from global_variable import PAGE_URL

import time 

class Scrapper():
    """Selenium window class"""
    def __init__(self,headless=False):
        self.wait_time:int = 5
        options = webdriver.ChromeOptions()
        options.add_argument('--log-level=1')
        options.add_argument("--log-level=3")
        # if len(str(print_pkl_info())) > 20:
        #     options.add_argument('headless')
        if headless:
            options.add_argument("headless")
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument("--start-maximized")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_page_load_timeout(15)

    def open_home_page(self):
        """A function that open the home page of the website"""
        self.driver.get(PAGE_URL)
    def get_id_of_an_element(self,page_id:str):
        """A function that get the id of an element"""
        page_id_element = WebDriverWait(self.driver,self.wait_time).until(
        EC.presence_of_element_located((By.ID, page_id)))
        return page_id_element.text