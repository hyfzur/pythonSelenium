import time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

hubUrl = "http://localhost:4444/wd/hub"
capsChrome = DesiredCapabilities.CHROME

driver = webdriver.Remote(command_executor=hubUrl,
                          desired_capabilities=capsChrome)

driver.get('http://demo.automationtesting.in/Frames.html')

driver.switch_to.frame("singleframe")

textBox = driver.find_element_by_css_selector(".col-xs-6 > input:nth-child(1)")
textBox.send_keys("iframe")

time.sleep(5)

driver.quit()
