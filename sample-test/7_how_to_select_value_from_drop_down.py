import time

from selenium import webdriver

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.select import Select

hubUrl = "http://localhost:4444/wd/hub"
capsChrome = DesiredCapabilities.CHROME

driver = webdriver.Remote(command_executor=hubUrl,
                          desired_capabilities=capsChrome)
driver.get('https://the-internet.herokuapp.com/dropdown')

# Find the element
dropDown = driver.find_element_by_id("dropdown")

# Initialize the element with the Select class
select = Select(dropDown)

# Pausing for 3 seconds using python's time module just for the tutorial.
# Not a recommended method to use in actual automation script development.
time.sleep(2)

# Select the first value from the drop down
select.select_by_index(1)
time.sleep(2)
print("Selected the first value")

# Select the second value from the drop down
select.select_by_value("2")
time.sleep(2)
print("Selected the second value")

# Select the first value from the drop down
select.select_by_visible_text("Option 1")
time.sleep(2)
print("Selected the first value")

driver.quit()