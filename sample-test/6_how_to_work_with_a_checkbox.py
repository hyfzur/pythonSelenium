import time

from selenium import webdriver
import pathlib

from selenium.webdriver import DesiredCapabilities

hubUrl = "http://localhost:4444/wd/hub"
capsChrome = DesiredCapabilities.CHROME

driver = webdriver.Remote(command_executor=hubUrl,
                          desired_capabilities=capsChrome)
driver.get('http://the-internet.herokuapp.com/checkboxes')

checkbox_1 = driver.find_element_by_css_selector("#checkboxes > input[type=checkbox]:nth-child(1)")

# Pausing for 3 seconds using python's time module just for the tutorial.
# Not a recommended method to use in actual automation script development.
time.sleep(2)
# This click will select the first checkbox
checkbox_1.click()

time.sleep(2)
print(checkbox_1.is_selected())

time.sleep(2)
# This click will unselect the first checkbox
checkbox_1.click()

time.sleep(2)
print(checkbox_1.is_selected())

driver.quit()

# Same approach can be used for Radio buttons
