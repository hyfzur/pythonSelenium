from selenium import webdriver
import pathlib

from selenium.webdriver import DesiredCapabilities

base_path = pathlib.Path(__file__).cwd().parent

hubUrl = "http://localhost:4444/wd/hub"
capsFirefox = DesiredCapabilities.FIREFOX

driver = webdriver.Remote(command_executor=hubUrl,
                          desired_capabilities=capsFirefox)
driver.get('http://automationpractice.com/index.php')
print(driver.title)
driver.quit()
