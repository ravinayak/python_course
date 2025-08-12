import re
import practice.book_locators_async.locators.locators as Locators

class BookParser:
    PRICE_PATTERN = r'£(\d+\.\d+)'
    RATING_MAP = {
		'One': 1,
		'Two': 2,
		'Three': 3,
		'Four': 4,
		'Five': 5,
	}

    def __init__(self, bs4):
        self.bs4 = bs4
        
    @property
    def href(self):
        href_locator = self.bs4.select_one(Locators.BOOK_HREF_LOCATOR)
        if not href_locator:
            return None
        else:
            return href_locator.get('href')
    
    @property    
    def star_rating(self):
        star_rating_locator = self.bs4.select_one(Locators.BOOK_STAR_RATING_LOCATOR)
        if not star_rating_locator:
            return None
        else:
            classes = star_rating_locator.get('class', [])
            if not classes:
                return None
            else:
                for class_name in classes:
                    if class_name in self.RATING_MAP:
                        return self.RATING_MAP[class_name]
                return None
    
    @property
    def title(self):
        title_locator = self.bs4.select_one(Locators.BOOK_TITLE_LOCATOR)
        if not title_locator:
            return None
        else:
            return title_locator.get('alt')
    
    @property    
    def stock_avail(self):
        stock_locator = self.bs4.select_one(Locators.BOOK_STOCK_LOCATOR)
        if not stock_locator:
            return None
        else:
            return stock_locator.text.strip()
    
    @property
    def price(self):
        price_locator = self.bs4.select_one(Locators.BOOK_PRICE_LOCATOR)
        if not price_locator:
            return None
        page_text = price_locator.text
        matches = re.match(self.PRICE_PATTERN, page_text)
        if matches:
            return float(matches.group(1))
        return None

    def __repr__(self):
        return (f'<href>: {self.href} '
		f'<star-rating>: {self.star_rating} '
        f'<title>: {self.title} '
        f'<stock_availability>: {self.stock_avail} '
        f'<price>: {self.price}')