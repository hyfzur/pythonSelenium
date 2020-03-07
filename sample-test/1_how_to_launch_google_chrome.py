from selenium import webdriver
import pathlib

from selenium.webdriver import DesiredCapabilities

base_path = pathlib.Path(__file__).cwd().parent

# Optional argument, if not specified will search path.
# driver = webdriver.Chrome(executable_path=(base_path / "drivers/chromedriver-80-mac").resolve())

hubUrl = "http://localhost:4444/wd/hub"
capsChrome = DesiredCapabilities.CHROME

driver = webdriver.Remote(command_executor=hubUrl,
                          desired_capabilities=capsChrome)

driver.get("http://automationpractice.com/index.php")
print(driver.title)
driver.quit()
