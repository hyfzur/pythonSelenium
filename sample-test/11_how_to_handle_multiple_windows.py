import time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

hubUrl = "http://localhost:4444/wd/hub"
capsChrome = DesiredCapabilities.CHROME

driver = webdriver.Remote(command_executor=hubUrl,
                          desired_capabilities=capsChrome)

driver.get('http://the-internet.herokuapp.com/windows')
first_window = driver.current_window_handle

print("First window: " + driver.title)

click_for_new_window = driver.find_element_by_css_selector(".example > a:nth-child(2)")
click_for_new_window.click()

all_window_handles = driver.window_handles

for handle in set(all_window_handles):
    if handle != first_window:
        driver.switch_to.window(handle)

print("Second window: " + driver.title)

driver.close()

driver.switch_to.window(first_window)

print("Default window: " + driver.title)

time.sleep(2)

driver.quit()
