"""Find elements with locators in Selenium WebDriver and check if it is found or not"""

from selenium import webdriver
import pathlib

from selenium.webdriver import DesiredCapabilities

hubUrl = "http://localhost:4444/wd/hub"
capsChrome = DesiredCapabilities.CHROME

driver = webdriver.Remote(command_executor=hubUrl,
                          desired_capabilities=capsChrome)
driver.get('http://automationpractice.com/index.php')

# Find an elements using class name
sale_banner = driver.find_elements_by_class_name("row")
print(len(sale_banner), " element(s) found with this class name")

# Find an elements using id
search_box = driver.find_elements_by_id("searchbox")
print(len(search_box), " element(s) found with this id")

# Find an elements using css selector
# The below selector find 7 elements on the page, however just returns 1 element when run via selenium.
# Something to look into.
popular_items = driver.find_elements_by_css_selector("[id='homefeatured'] [class='product-container']")
print(len(search_box), " element(s) found with this css selector")
# Check this link for more info on css selectors: https://saucelabs.com/resources/articles/selenium-tips-css-selectors

# Find an elements using link text
more_links = driver.find_elements_by_link_text("More")
print(len(more_links), " element(s) found with this link text")

# Find an elements using partial link text
add_to_cart = driver.find_elements_by_partial_link_text("Add to")
print(len(add_to_cart), " element(s) found with this partial link text")

# Find an elements using name
submit_button = driver.find_elements_by_name("submit_search")
print(len(submit_button), " element(s) found with this name")

# Find an elements using xpath
popular_items_again = driver.find_elements_by_xpath("//*[@id='homefeatured']//li")
print(len(popular_items_again), " element(s) found with this xpath")

# Find an elements using tag name
li_tags = driver.find_elements_by_tag_name("li")
print(len(li_tags), " element(s) found with this xpath")

driver.quit()
