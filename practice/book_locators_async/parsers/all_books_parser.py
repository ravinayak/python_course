import practice.book_locators_async.locators.locators as Locators
from practice.book_locators_async.parsers.book_parser import BookParser

class AllBooksParser:
    PAGE_NUM_PATTERN = r'\s+Page \d+ of (\d+)\s+'

    def __init__(self, bs4):
        self.bs4 = bs4

    def parse_books(self):
        book_locators = self.bs4.select(Locators.BOOKS_LOCATOR)
        book_parsers = []
        for book_locator in book_locators:
            book_parsers.append(BookParser(book_locator))
        return book_parsers
            
    
        
        
        
        