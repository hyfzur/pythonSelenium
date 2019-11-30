from selenium import webdriver
import pathlib

base_path = pathlib.Path(__file__).cwd().parent

driver = webdriver.Chrome(executable_path=(base_path / "drivers/chromedriver-v77").resolve())  # Optional argument, if not specified will search path.
driver.get('http://automationpractice.com/index.php')

driver.close()

