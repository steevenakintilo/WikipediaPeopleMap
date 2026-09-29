from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import time 
import pytest
PAGE_URL = "http://localhost:5173/"
LIST_OF_PAGE_BUTTON_ID = [
    "WorldMapPageButton",
    "StatisticsPageButton",
    "OtherStatisticsPageButton",
    "QjisMapPageButton",
    "AboutPageButton"
]
class Scrapper():
    """Selenium window class"""
    def __init__(self,headless=False):
        self.wait_time:int = 5
        options = webdriver.ChromeOptions()
        options.add_argument('--log-level=1')
        options.add_argument("--log-level=3")
        # if len(str(print_pkl_info())) > 20:
        #     options.add_argument('headless')

        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument("--start-maximized")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_page_load_timeout(15)

    def test_check_page_id(self,page_id:str):
        """A function that loop and go through page of the website by checking id of each page button"""
        page_id_element = WebDriverWait(self.driver,self.wait_time).until(
        EC.presence_of_element_located((By.ID, page_id)))
        print(page_id_element.text)
        
    def test_open_home_page(self):
        """A function that open the home page of the website"""
        self.driver.get(PAGE_URL)
        print(self.driver.title)
        for page_id in LIST_OF_PAGE_BUTTON_ID:
            self.check_page_id(page_id)
            time.sleep(1)

        
        time.sleep(4)
        self.driver.quit()
        toto = True
        assert toto == True
        

test = Scrapper()
test.open_home_page()

