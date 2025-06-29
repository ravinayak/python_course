from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from parsers.quote_selection_selenium.locators.quote_locators import QUOTE_LOCATOR_TUPLE
from parsers.quote_selection_selenium.config import Config
from parsers.quote_selection_selenium.exceptions.quote_search_exceptions import QuoteNotFoundException

class QuoteParser:
    
    config = Config()

    def __init__(self, browser_object):
        self.browser_object = browser_object
        
    @property
    def quote(self):
        try:
            WebDriverWait(self.browser_object, self.config.max_wait_time).until(
				expected_conditions.presence_of_element_located(
					(By.CSS_SELECTOR, QUOTE_LOCATOR_TUPLE[1])
				)
			)
            return self.browser_object.find_element(*QUOTE_LOCATOR_TUPLE).text.strip()
        except(TimeoutException, NoSuchElementException):
            QuoteNotFoundException('Quote was not found', 500)
