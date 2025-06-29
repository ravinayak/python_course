from parsers.quote_parsers_selenium.locators.quote_locators import QUOTE_TEXT_TUPLE, QUOTE_AUTHOR_TUPLE, QUOTE_TAGS, QUOTE_TAG_LINK
from selenium.webdriver.common.by import By

class QuoteParser:
    
    def __init__(self, quote_browser_obj):
        self.quote_browser_obj = quote_browser_obj
        
    def __repr__(self):
        return(
			f'<Quote Text :: {self.text}; '
			f'Author :: {self.author}; '
			f'Tags :: {self.tags}; '
			f'Link :: {self.link}> \n'
		)

    @property
    def text(self):
        locator = self.quote_browser_obj.find_element(*QUOTE_TEXT_TUPLE)
        return locator.text if locator else None
    
    @property
    def author(self):
        locator = self.quote_browser_obj.find_element(*QUOTE_AUTHOR_TUPLE)
        return locator.text if locator else None
    
    @property
    def tags(self):
        locator = self.quote_browser_obj.find_element(By.CSS_SELECTOR, QUOTE_TAGS)
        if not locator:
            return ''
        tags = locator.get_attribute('content')
        return ', '.join([tag.strip() for tag in tags.split(',')]) if tags else ''
    
    @property
    def link(self):
        locator = self.quote_browser_obj.find_element(By.CSS_SELECTOR, QUOTE_TAG_LINK)
        return locator.get_attribute('href') if locator else None