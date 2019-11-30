from selenium import webdriver
import pathlib

base_path = pathlib.Path(__file__).cwd().parent

driver = webdriver.Firefox(executable_path=(
        base_path / "drivers/geckodriver-v0_26_0").resolve())  # Optional argument, if not specified will search path.
driver.get('http://automationpractice.com/index.php')

driver.close()
