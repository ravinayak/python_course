import re
from urllib.parse import urljoin
from parsers.book_parsers.locators.book_locators import BOOK_LINK_LOCATOR, BOOK_NAME_LOCATOR, BOOK_RATING_LOCATOR, BOOK_PRICE_LOCATOR, BOOK_STOCK_AVAILABILITY

class BookParser:
    
    def __init__(self, book_object, page_url: str):
        self.book_object = book_object
        self.page_url = page_url

    def __repr__(self):
        return (
            f'<Book: "{self.name or "N/A"}", '
            f'Price: £{self.price or "N/A"}, '
            f'Rating: {self.rating or "N/A"}/Five, '
            f'Available: {self.stock_availability or "N/A" }, '
            f'Link: {self.link or "N/A"}>'
        )
        
    @property
    def link(self):
        locator = self.book_object.select_one(BOOK_LINK_LOCATOR)
        relative_link = locator.get('href') if locator else None
        if not relative_link:
            return None
        # Create a full, absolute URL from the page's URL and the relative link.
        return urljoin(self.page_url, relative_link)
        
    @property
    def name(self):
        locator = self.book_object.select_one(BOOK_NAME_LOCATOR)
        return locator.attrs.get('title') if locator else None
        
    @property
    def rating(self):
        locator = self.book_object.select_one(BOOK_RATING_LOCATOR)
        classes = locator.get('class', []) if locator else []
        rating_class = next((c for c in classes if c != 'star-rating'), None)
        return rating_class
    
    @property
    def price(self):
        locator = self.book_object.select_one(BOOK_PRICE_LOCATOR)
        price_str = locator.string if locator else ''
        pattern = r'£(\d+\.?\d+)'
        match = re.search(pattern, price_str)
        return float(match.group(1)) if match else None
    
    @property
    def stock_availability(self):
        locator = self.book_object.select_one(BOOK_STOCK_AVAILABILITY)
        return locator.text.strip() if locator else None