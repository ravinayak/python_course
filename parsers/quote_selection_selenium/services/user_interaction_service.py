from parsers.quote_selection_selenium.parsers.quote_search_parser import QuoteSearchParser
from parsers.quote_selection_selenium.parsers.quote_parser import QuoteParser

class UserInteractionService:
    
    def __init__(self, browser_object):
        self.browser_object = browser_object
        self.quote_search_obj = QuoteSearchParser(browser_object = browser_object)
        
    def author_search(self):
        authors = self.quote_search_obj.authors
        print('Please select from one of these authors :: \n [{}]\n ::'.format(' | '.join(authors)), end = " ")
        author_input = input().strip()
        self.quote_search_obj.select_author(author = author_input)

    def tag_search(self):
        tags = self.quote_search_obj.tags
        print(' Please select from one of these tags :: \n [{}]\n ::'.format(' | '.join(tags)), end = " ")
        tag_input = input().strip()
        self.quote_search_obj.select_tag(tag = tag_input)
    
    def retrieve_tag(self):
        quote = QuoteParser(browser_object = self.browser_object).quote or None
        print(f'Quote is :: {quote}')
        return quote

    def prompt_for_search(self):
        self.author_search()
        self.tag_search()
        self.quote_search_obj.click_search
        self.retrieve_tag()
        
