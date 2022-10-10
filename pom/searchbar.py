from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Searchbar:
    item_srch_id = 'iname'
    mob_srch_id = 'mob_name'
    skill_srch_id = 'sk_name'
    renewal_check_id = 'qs_page'

    def __init__(self, driver):
        self.driver = driver

    def search_for_item(self, item):
        item_srch = self.driver.find_element(By.NAME, self.item_srch_id)
        item_srch.send_keys(item)
        item_srch.send_keys(Keys.ENTER)

    def search_for_mob(self, mob):
        mob_srch = self.driver.find_element(By.NAME, self.mob_srch_id)
        mob_srch.send_keys(mob)
        mob_srch.send_keys(Keys.ENTER)

    def search_for_skill(self, skill):
        skill_srch = self.driver.find_element(By.NAME, self.skill_srch_id)
        skill_srch.send_keys(skill)
        skill_srch.send_keys(Keys.ENTER)