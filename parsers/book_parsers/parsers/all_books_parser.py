from bs4 import BeautifulSoup
from parsers.book_parsers.locators.all_books_locators import ALL_BOOKS_LOCATORS
from parsers.book_parsers.parsers.book_parser import BookParser

class AllBooksParser:
    
    def __init__(self, page_content: str, page_url: str):
        self.soup = BeautifulSoup(page_content, 'html.parser')
        self.page_url = page_url
        
    @property
    def books(self):
        """
        Returns a list of BookParser objects, one for each book found on the page.
        """
        # Use .select() to find all matching elements, not just the first one.
        book_elements = self.soup.select(ALL_BOOKS_LOCATORS)
        return [BookParser(book, self.page_url) for book in book_elements]