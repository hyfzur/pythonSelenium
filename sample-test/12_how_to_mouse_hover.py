import time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, ActionChains

hubUrl = "http://localhost:4444/wd/hub"
capsChrome = DesiredCapabilities.CHROME

driver = webdriver.Remote(command_executor=hubUrl,
                          desired_capabilities=capsChrome)

# Static tooltip
driver.get('https://www.google.com/')
google_apps = driver.find_element_by_css_selector(".gb_D")
print((google_apps.get_attribute("title")))

# Dynamic tooltip
driver.get('http://the-internet.herokuapp.com/hovers')
avatar = driver.find_element_by_class_name("figure")

action = ActionChains(driver)
action.move_to_element(avatar).perform()

time.sleep(8)

info = driver.find_element_by_class_name("figcaption")
print(info.is_displayed())

driver.quit()
