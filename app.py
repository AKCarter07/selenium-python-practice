# pip instal selenium
from selenium import webdriver
import time
from pom.searchbar import Searchbar
from pom.searchResults import SearchResults

driver = webdriver.Chrome('chromedriver.exe')

driver.get("https://ratemyserver.net")
searchbar = Searchbar(driver)
results = SearchResults(driver)

# time.sleep(2)

# searchbar.search_for_mob('poring')
# time.sleep(2)
# results.multipage()
searchbar.search_for_mob('goblin')
# time.sleep(3)
results.multipage()


time.sleep(2)
driver.quit()
