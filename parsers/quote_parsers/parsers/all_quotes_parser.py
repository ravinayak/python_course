from bs4 import BeautifulSoup
from parsers.quote_parsers.locators.all_quote_locators import ALL_QUOTE_LOCATORS
from parsers.quote_parsers.parsers.quote_parser import QuoteParser

class AllQuotesParser:
    
    def __init__(self, page: str, url: str):
        self.soup = BeautifulSoup(page, 'html.parser')
        self.url = url
    
    @property
    def quotes(self):
        all_quotes = self.soup.select(ALL_QUOTE_LOCATORS)
        for quote in all_quotes:
            print(QuoteParser(quote, self.url))
        return [QuoteParser(quote, self.url) for quote in all_quotes]