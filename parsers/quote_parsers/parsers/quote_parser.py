from parsers.quote_parsers.locators.quote_locator import QUOTE_TEXT, QUOTE_AUTHOR, QUOTE_TAGS, QUOTE_TAG_LINKS
from urllib.parse import urljoin
class QuoteParser:
    
    def __init__(self, quote_bs_object, url):
        self.quote_bs_object = quote_bs_object
        self.url = url
        
    def __repr__(self):
        tag_link_str = ', '.join(
			f'{tag} -> {urljoin(self.url, link).rstrip('/')}'
			for tag, link in self.tag_links.items()
		)
            
        return(
			f'<Quote Text :: {self.text}; '
			f'Author :: {self.author}; '
			f'Tags :: {self.tags}; '
			f'TagLinks :: {tag_link_str}>'
		)
        
    @property
    def text(self):
        quote_text = self.quote_bs_object.select_one(QUOTE_TEXT)
        return quote_text.string.strip() if quote_text else None
    
    @property
    def author(self):
        quote_author = self.quote_bs_object.select_one(QUOTE_AUTHOR)
        return quote_author.string.strip() if quote_author else None
    
    @property
    def tags(self):
        quote_tag_obj = self.quote_bs_object.select_one(QUOTE_TAGS)
        if not quote_tag_obj:
            return ''  # Return an empty string for type consistency.
        
        content = quote_tag_obj.get('content', '')
        separator = ', '
        return separator.join([tag.strip() for tag in content.split(',') if tag.strip()])
        
    @property
    def tag_links(self):
        quote_tag_links = self.quote_bs_object.select(QUOTE_TAG_LINKS)
        return {
			tag.string.strip(): tag.get('href', None) for tag in quote_tag_links
		}