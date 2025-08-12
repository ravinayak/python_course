import re
from bs4 import BeautifulSoup
from unsync import unsync
import async_timeout
import aiohttp
import practice.book_locators_async.locators.locators as Locators
import practice.book_locators_async.config as Config
from practice.book_locators_async.parsers.all_books_parser import AllBooksParser

class AllBooksObjects:
    PAGE_NUM_PATTERN = r'\s+Page \d+ of (\d+)\s+'

    def __init__(self, page):
        self.bs4 = BeautifulSoup(page, 'html.parser')
        self.page_num = 0

    def parse_page_num(self):
        page_text = self.bs4.select_one(Locators.PAGER_LOCATOR).text
        matches = re.match(self.PAGE_NUM_PATTERN, page_text)
        if matches:
            return int(matches.group(1))
        else:
            return None
    
    @unsync
    async def download_book_pages(self, url):
        async with aiohttp.ClientSession() as session:
            async with async_timeout.timeout(Config.ASYNC_TIMEOUT):
                async with session.get(url) as response:
                    return { url: await response.text() }

    def prep_all_books_parsers(self, content_dict, all_books_parsers):
        for _, page_html in content_dict.items():
            all_books_parsers.append(AllBooksParser(BeautifulSoup(page_html, 'html.parser')))

        return all_books_parsers
    
    async def process_pages(self, page_limit):
        all_books_parsers = []
        urls = []
        content_dict = {}

        for page_num in range(1, page_limit + 1):
            urls.append(Config.BOOK_PAGE_URL.format(page_num))

        futures = [self.download_book_pages(url) for url in urls]
        
        for f in futures:
            content_url_dict = f.result()
            content_dict.update(content_url_dict)

        return self.prep_all_books_parsers(content_dict, all_books_parsers)
        
        
        
        