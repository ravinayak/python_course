import re
import logging
from urllib.parse import urljoin
from parsers.books_with_pages_parsers.locators.book_locators import LINK_LOCATOR, NAME_LOCATOR, RATING_LOCATOR, PRICE_LOCATOR, STOCK_AVAILABILITY

logger = logging.getLogger('pagescraper.book_parser')
class BookParser:
    
    def __init__(self, book, url: str):
        self.book = book
        self.url = url
        
    def __repr__(self):
        return(
            f'<Book Name :: {self.name or "N/A"}; '
            f'Link :: {self.link or "N/A"}; '
            f'Price :: £{self.price or "N/A"}; '
            f'Rating :: {self.rating or "N/A"}; '
            f'Stock :: {self.stock or "N/A"}>'
        )
        
    @property
    def rating(self):
        logger.info(' Accessing Rating for book')
        locator = self.book.select_one(RATING_LOCATOR)
        if not locator:
            return None
        classes = locator.get('class', [])
        return [class_str.strip() for class_str in classes if class_str != 'star-rating'][0]
        
    @property
    def price(self):
        logger.info(' Accessing Price for book')
        pattern = r'£(\d+\.?\d+)'
        locator = self.book.select_one(PRICE_LOCATOR)
        if not locator:
            return None
        search_str = locator.string.strip()
        match = re.search(pattern, search_str)
        return float(match[1]) if match else ''
        
    @property
    def link(self):
        logger.info(' Accessing Link for book')
        locator = self.book.select_one(LINK_LOCATOR)
        if not locator:
            return None
        relative_link = locator.get('href', None)
        return urljoin(self.url, relative_link)
        
    @property
    def name(self):
        logger.info(' Accessing Name for book')
        locator = self.book.select_one(NAME_LOCATOR)
        if not locator:
            return None
        return locator.get('title', None)
        
    @property
    def stock(self):
        logger.info(' Accessing Stock Availability for book')
        locator = self.book.select_one(STOCK_AVAILABILITY)
        if not (locator or locator.text):
            return None
        return locator.text.strip()