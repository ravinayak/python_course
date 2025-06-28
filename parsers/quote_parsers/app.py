import requests
from parsers.quote_parsers.parsers.all_quotes_parser import AllQuotesParser

URL = 'https://quotes.toscrape.com/'

page = requests.get(URL)

def run():
    all_quotes = AllQuotesParser(page = page.content, url = URL)
    return all_quotes.quotes

run()
