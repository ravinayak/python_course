from selenium import webdriver
from parsers.quote_parsers_selenium.pages.all_quotes import AllQuotes

URL = 'https://quotes.toscrape.com/'


def run():
    # Get a chrome instance which will interact with Chrome Browser
	# for UI tests
	chrome = webdriver.Chrome()

	# This will load the webpage in chrome instance of the driver
	chrome.get(URL)
	AllQuotes(browser_obj = chrome).quotes

 
if __name__ == '__main__':
    run()

