from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from global_variable import PAGE_URL


class Scrapper():
    """Selenium window class"""
    def __init__(self, headless=False):
        self.wait_time: int = 10
        options = webdriver.ChromeOptions()
        options.add_argument("--log-level=3")
        if headless:
            options.add_argument("--headless=new")
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # Taille fixe : les boutons "desktop_only" du site sont cachés sur petit écran
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_page_load_timeout(15)

    def open_home_page(self):
        """A function that open the home page of the website"""
        self.driver.get(PAGE_URL)

    def get_title(self) -> str:
        """A function that return the title of the current page"""
        return self.driver.title

    def get_current_path(self) -> str:
        """A function that return the path of the current url (ex: /About)"""
        return self.driver.execute_script("return window.location.pathname")

    def get_element(self, element_id: str):
        """A function that wait for an element to be visible and return it"""
        return WebDriverWait(self.driver, self.wait_time).until(
            EC.visibility_of_element_located((By.ID, element_id)))

    def get_id_of_an_element(self, element_id: str) -> str:
        """A function that get the text of an element from its id"""
        return self.get_element(element_id).text

    def click_on_element(self, element_id: str):
        """A function that click on an element from its id"""
        WebDriverWait(self.driver, self.wait_time).until(
            EC.element_to_be_clickable((By.ID, element_id))).click()

    def wait_for_path(self, path: str) -> bool:
        """A function that wait until the browser is on the given path"""
        return WebDriverWait(self.driver, self.wait_time).until(
            lambda driver: driver.execute_script("return window.location.pathname") == path)

    def count_elements(self, css_selector: str) -> int:
        """A function that count the elements matching a css selector"""
        return len(self.driver.find_elements(By.CSS_SELECTOR, css_selector))

    def go_back(self):
        """A function that go back to the previous page"""
        self.driver.back()

    def quit(self):
        """A function that close the browser"""
        self.driver.quit()
