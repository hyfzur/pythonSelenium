import time

from selenium import webdriver
import pathlib

from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.common.keys import Keys

hubUrl = "http://localhost:4444/wd/hub"
capsChrome = DesiredCapabilities.CHROME

driver = webdriver.Remote(command_executor=hubUrl,
                          desired_capabilities=capsChrome)
driver.get('http://the-internet.herokuapp.com/')

testElement = driver.find_element_by_tag_name("h2")
action = ActionChains(driver)
action.move_to_element(testElement).context_click().perform()
# Below commands are not working !!!
action.send_keys(Keys.ARROW_RIGHT)
action.send_keys(Keys.ARROW_DOWN)


time.sleep(2)

driver.quit()
