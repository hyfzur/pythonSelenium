import time

from selenium import webdriver
import pathlib

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.select import Select
hubUrl = "http://localhost:4444/wd/hub"
capsChrome = DesiredCapabilities.CHROME

driver = webdriver.Remote(command_executor=hubUrl,
                          desired_capabilities=capsChrome)

driver.get('http://the-internet.herokuapp.com/javascript_alerts')

# Element to access the js alert
# jsAlert = driver.find_element_by_id("#content > div > ul > li:nth-child(1) > button")
jsAlert = driver.find_element_by_css_selector(".example li:nth-child(1) button")
jsConfirm = driver.find_element_by_css_selector(".example li:nth-child(2) button")
jsPrompt = driver.find_element_by_css_selector(".example li:nth-child(3) button")

# The click action will trigger a js alert
jsAlert.click()
alert = driver.switch_to.alert
print(alert.text)

time.sleep(2)
alert.accept()

# The click action will trigger a js confirm
jsConfirm.click()
time.sleep(2)
confirm = driver.switch_to.alert
print(confirm.text)
confirm.dismiss()
jsConfirm.click()
time.sleep(2)
confirm.accept()

# The click action will trigger a js prompt
jsPrompt.click()
prompt = driver.switch_to.alert
print(prompt.text)
time.sleep(2)
prompt.dismiss()
time.sleep(2)
jsPrompt.click()
# The sendkeys is not working, will look into this later
prompt.send_keys("Entering text in the prompt")
time.sleep(2)
prompt.accept()

driver.quit()
