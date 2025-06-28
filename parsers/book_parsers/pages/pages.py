import requests
from parsers.book_parsers.parsers.all_books_parser import AllBooksParser

URL = 'http://books.toscrape.com'

class Pages:
    @classmethod
    def fetch_books(self):
        """
        Fetches the page content, parses it, and returns a list of book objects.
        This method is self-contained and does not rely on class state.
        """
        response = requests.get(URL)
        response.raise_for_status()  # It's good practice to check for request errors
        # Pass both the content and the final URL (after any redirects) to the parser.
        return AllBooksParser(response.content, response.url).books