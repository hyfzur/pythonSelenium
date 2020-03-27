from selenium import webdriver

from selenium.webdriver import DesiredCapabilities

hubUrl = "http://localhost:4444/wd/hub"
capsChrome = DesiredCapabilities.CHROME

driver = webdriver.Remote(command_executor=hubUrl,
                          desired_capabilities=capsChrome)

driver.get("http://automationpractice.com/index.php")
print(driver.title)
driver.quit()
