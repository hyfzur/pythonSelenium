import pathlib

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

file_path = pathlib.Path(__file__).cwd().parent / "docker/how_to_run_docker_selenium"

hubUrl = "http://localhost:4444/wd/hub"
capsChrome = DesiredCapabilities.CHROME

driver = webdriver.Remote(command_executor=hubUrl,
                          desired_capabilities=capsChrome)

# driver.file_detector()
driver.get('http://the-internet.herokuapp.com/upload')

choose_file = driver.find_element_by_id("file-upload")
upload = driver.find_element_by_id("file-submit")

choose_file.send_keys(file_path)

driver.quit()
