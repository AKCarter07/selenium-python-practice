from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchResults:
    next_page_title = 'Next page'

    def __init__(self, driver):
        self.driver = driver

# Well this doesn't want to work
    def multipage(self):
        try:
            print(f"//tagname[@title='{self.next_page_title}']")
            next_page = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//tagname[@title='Next page']")))
            print("next_page")
        except:
            print("false")

