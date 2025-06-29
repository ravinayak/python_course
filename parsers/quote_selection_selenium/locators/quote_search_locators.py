from selenium.webdriver.common.by import By

AUTHOR_LOCATOR_TUPLE = (By.CSS_SELECTOR, 'div.container form div.row div.col-md-4.form-group select#author')
TAG_LOCATOR_TUPLE = (By.CSS_SELECTOR, 'div.container form div.row div.col-md-4.form-group select#tag')
SEARCH_LOCATOR_TUPLE = (By.CSS_SELECTOR, 'div.container form input[name="submit_button"]')