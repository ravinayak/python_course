from selenium.webdriver.common.by import By

QUOTE_TEXT_TUPLE = (By.CSS_SELECTOR, 'div.quote span.text')
QUOTE_AUTHOR_TUPLE = (By.CSS_SELECTOR, 'div.quote span small.author')
QUOTE_TAGS = 'div.quote div.tags meta.keywords' # attribute content
QUOTE_TAG_LINK = 'div.quote div.tags a.tag' # attribute href