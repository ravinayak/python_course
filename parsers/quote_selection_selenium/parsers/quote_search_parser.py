from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from parsers.quote_selection_selenium.config import Config
from parsers.quote_selection_selenium.locators.quote_search_locators import AUTHOR_LOCATOR_TUPLE, TAG_LOCATOR_TUPLE, SEARCH_LOCATOR_TUPLE
from parsers.quote_selection_selenium.exceptions.quote_search_exceptions import AuthorNotFoundException, TagNotFoundException

class QuoteSearchParser:
    
    config = Config()

    def __init__(self, browser_object):
        self.browser_object = browser_object
        
    @property
    def author_select_object(self):
        try:
            locator = self.browser_object.find_element(*AUTHOR_LOCATOR_TUPLE)
            WebDriverWait(self.browser_object, self.config.max_wait_time).until(
				expected_conditions.presence_of_element_located(
					(By.CSS_SELECTOR, AUTHOR_LOCATOR_TUPLE[1] + ' option[value]')
				)
			)
            return Select(locator)
        except(TimeoutException, NoSuchElementException):
            print('Element was not found, exception occurred')
            raise AuthorNotFoundException('Author Element was not found', 500)
        
    @property
    def authors(self):
        return [option.text.strip() for option in self.author_select_object.options]
    
    @property
    def tag_select_object(self):
        try:
            locator = self.browser_object.find_element(*TAG_LOCATOR_TUPLE)
            WebDriverWait(self.browser_object, self.config.max_wait_time).until(
                expected_conditions.presence_of_element_located(
                    (By.CSS_SELECTOR, TAG_LOCATOR_TUPLE[1] + ' option[value]')
                )
            )
            return Select(locator)
        except(TimeoutException, NoSuchElementException):
            print('No Element with tag was found')
            raise TagNotFoundException('Tag Element was not found', 500)
        
    @property
    def tags(self):
        return [option.text.strip() for option in self.tag_select_object.options]
    
    def select_tag(self, tag: str):
        locator = self.browser_object.find_element(*TAG_LOCATOR_TUPLE)
        Select(locator).select_by_visible_text(tag)
        
    def select_author(self, author: str):
        locator = self.browser_object.find_element(*AUTHOR_LOCATOR_TUPLE)
        Select(locator).select_by_visible_text(author)
        
    @property
    def click_search(self):
        self.browser_object.find_element(*SEARCH_LOCATOR_TUPLE).click()
        
        
        
    