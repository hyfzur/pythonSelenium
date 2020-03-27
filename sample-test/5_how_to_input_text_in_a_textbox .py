import time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

hubUrl = "http://localhost:4444/wd/hub"
capsChrome = DesiredCapabilities.CHROME

driver = webdriver.Remote(command_executor=hubUrl,
                          desired_capabilities=capsChrome)
driver.get('http://automationpractice.com/index.php')

search_box = driver.find_element_by_id("search_query_top")
search_box.send_keys("typing in the search box")

# Pausing for 3 seconds using python's time module just for the tutorial.
# Not a recommended method to use in actual automation script development.
time.sleep(3)
driver.quit()
