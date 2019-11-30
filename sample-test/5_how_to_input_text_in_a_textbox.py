import time

from selenium import webdriver
import pathlib

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

base_path = pathlib.Path(__file__).cwd().parent

driver = webdriver.Chrome(executable_path=(
        base_path / "drivers/chromedriver-v77").resolve())  # Optional argument, if not specified will search path.
driver.maximize_window()
driver.get('http://the-internet.herokuapp.com/')

testElement = driver.find_element_by_tag_name("h2")
action = ActionChains(driver)
action.move_to_element(testElement).context_click().perform()
# Below commands are not working !!!
action.send_keys(Keys.ARROW_RIGHT)
action.send_keys(Keys.ARROW_DOWN)


time.sleep(2)

driver.close()
