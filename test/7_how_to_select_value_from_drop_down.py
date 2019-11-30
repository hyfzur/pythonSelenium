import time

from selenium import webdriver
import pathlib

from selenium.webdriver.support.select import Select

base_path = pathlib.Path(__file__).cwd().parent

driver = webdriver.Chrome(executable_path=(
        base_path / "drivers/chromedriver-v77").resolve())  # Optional argument, if not specified will search path.
driver.maximize_window()
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

driver.close()