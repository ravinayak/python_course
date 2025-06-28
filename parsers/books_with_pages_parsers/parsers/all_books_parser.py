from bs4 import BeautifulSoup
import logging
import requests
from parsers.books_with_pages_parsers.locators.all_books_locators import ALL_BOOKS_LOCATORS
from parsers.books_with_pages_parsers.parsers.book_parser import BookParser

logger = logging.getLogger('pagescraper.all_book_parser')
class AllBooksParser:
    
    def __init__(self, url: str):
        self.url = url
        self.page_content = requests.get(url).content
        self.soup = BeautifulSoup(self.page_content, 'html.parser')
    
    @property
    def books(self):
        logger.info(' Accessing all books for the page')
        book_objects = self.soup.select(ALL_BOOKS_LOCATORS)
        if not book_objects:
            return []
        return [BookParser(book = book_object, url = self.url) for book_object in book_objects]