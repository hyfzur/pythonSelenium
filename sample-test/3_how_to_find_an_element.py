"""Find elements with locators in Selenium WebDriver and check if it is found or not"""

from selenium import webdriver
import pathlib

base_path = pathlib.Path(__file__).cwd().parent

driver = webdriver.Chrome(executable_path=(
        base_path / "drivers/chromedriver-v77").resolve())  # Optional argument, if not specified will search path.
driver.get('http://automationpractice.com/index.php')

# Find an element using class name
sale_banner = driver.find_element_by_class_name("img-responsive")
print("Sale banner present? ", sale_banner.is_enabled())

# Find an element using id
search_box = driver.find_element_by_id("searchbox")
print("Search box present? ", search_box.is_enabled())

# Find an element using css selector
top_menu = driver.find_element_by_css_selector("#block_top_menu")
print("Top menu present? ", top_menu.is_enabled())
# Check this link for more info on css selectors: https://saucelabs.com/resources/articles/selenium-tips-css-selectors

# Find an element using link text
specials = driver.find_element_by_link_text("Specials")
print("Specials present? ", specials.is_enabled())

# Find an element using partial link text
terms_and_conditions = driver.find_element_by_partial_link_text("Terms")
print("Terms and Conditions present? ", terms_and_conditions.is_enabled())

# Find an element using name
submit_button = driver.find_element_by_name("submit_search")
print("Submit button present? ", submit_button.is_enabled())

# Find an element using xpath
shopping_cart = driver.find_element_by_xpath("//*[@id='header']/div[3]/div/div/div[3]/div/a")
print("Shopping cart present? ", shopping_cart.is_enabled())

# Find an element using tag name
footer = driver.find_element_by_tag_name("footer")
print("Footer present? ", shopping_cart.is_enabled())


driver.close()
