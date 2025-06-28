import requests
from bs4 import BeautifulSoup
import re
from parsers.books_with_pages_parsers.locators.all_books_locators import ALL_BOOKS_PAGER_LOCATOR

class AllPages:
    
    def __init__(self, url: str):
        page_content = requests.get(url).content
        self.soup = BeautifulSoup(page_content, 'html.parser')
        
    @property
    def total_pages(self):
        pattern = r'Page \d+ of (\d+)'
        locator = self.soup.select_one(ALL_BOOKS_PAGER_LOCATOR)
        if not locator:
            return None
        search_str = locator.string.strip()
        match = re.search(pattern, search_str)
        return int(match[1]) if match else 1
            
            
        
        
        
        