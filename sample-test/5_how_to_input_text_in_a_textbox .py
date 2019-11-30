import time

from selenium import webdriver
import pathlib

base_path = pathlib.Path(__file__).cwd().parent

driver = webdriver.Chrome(executable_path=(
        base_path / "drivers/chromedriver-v77").resolve())  # Optional argument, if not specified will search path.
driver.get('http://automationpractice.com/index.php')

search_box = driver.find_element_by_id("search_query_top")
search_box.send_keys("typing in the search box")

# Pausing for 3 seconds using python's time module just for the tutorial.
# Not a recommended method to use in actual automation script development.
time.sleep(3)
driver.close()
