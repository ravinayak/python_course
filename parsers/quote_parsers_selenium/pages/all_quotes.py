from parsers.quote_parsers_selenium.locators.all_quotes_locators import ALL_QUOTES_LOCATOR_TUPLE
from parsers.quote_parsers_selenium.parsers.quote_parser import QuoteParser
class AllQuotes:
    
    def __init__(self, browser_obj):
        self.browser_obj = browser_obj
    
    @property
    def quotes(self):
        quotes_obj = self.browser_obj.find_elements(*ALL_QUOTES_LOCATOR_TUPLE)
        print('\n\t\t\t\t\t *********************** Quotes ***********************\n')
        for quote_obj in quotes_obj:
            print(QuoteParser(quote_browser_obj = quote_obj), end="")
        print('\n\t\t\t\t\t ******************************************************\n')
    