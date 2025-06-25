from bs4 import BeautifulSoup
import re

ITEM_HTML = '''<html><head>This is the Title</head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
        <div class="image_container">
                <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
        </div>
        <p class="star-rating Three">
            <i class="icon-star">One</i>
            <i class="icon-star">Two</i>
            <i class="icon-star">Three</i>
            <i class="icon-star">Four</i>
            <i class="icon-star">Five</i>
        </p>
        <h3>
            <a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">
                A Light in the ...
            </a>
        </h3>
        <div class="product_price">
            <p class="price_color">£51.77</p>
            <p class="instock availability">
                <i class="icon-ok"></i>
                In stock
            </p>
            <form>
                <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
            </form>
        </div>
    </article>
</li>

</body></html>
'''

class ParsedItem:
  
  HEAD_LOCATOR = 'html head'
  LINK_LOCATOR = 'article.product_pod div.image_container a'
  CONTENT_LOCATOR = 'article.product_pod div.image_container a img'
  RATING_LOCATOR = 'article.product_pod p.star-rating'
  LI_ITEMS_LOCATOR = 'article.product_pod p.star-rating li.icon-star'
  H3_TITLE = 'article.product_pod h3 a'
  PRICE_LOCATOR = 'article.product_pod div.product_price p.price_color'
  
  def __init__(self, page: str = None):
    self.soup = BeautifulSoup(page, 'html.parser')

  @property
  def title(self):
    title_val = self.soup.select_one(ParsedItem.HEAD_LOCATOR).string
    print(title_val)
    return title_val

  @property
  def link(self):
    link_val = self.soup.select_one(ParsedItem.LINK_LOCATOR).get('href')
    print(link_val)
    return link_val

  @property
  def content(self):
    content_val = self.soup.select_one(ParsedItem.CONTENT_LOCATOR).attrs['alt']
    print(content_val)
    return content_val

  @property
  def li_items(self):
    li_items_arr = self.soup.select(ParsedItem.LI_ITEMS_LOCATOR)
    li_items_val = [li_item.string for li_item in li_items_arr]
    print(li_items_val)
    return li_items_val

  @property
  def h3_title(self):
    h3_title_val = self.soup.select_one(ParsedItem.H3_TITLE).attrs['title']
    print(h3_title_val)
    return h3_title_val

  @property
  def price(self):
    price_val = self.soup.select_one(ParsedItem.PRICE_LOCATOR).string
    pattern = r'£(\d+\.?\d+)'
    match = re.search(pattern, price_val)
    float_price = float(match[1])
    print(f'Price is :: {float_price}')
    return float_price

  @property
  def rating(self):
    classes = self.soup.select_one(ParsedItem.RATING_LOCATOR).get('class', [])
    rating_val = filter(lambda x: x != 'star-rating', classes)
    print(rating_val)
    return rating_val

  @property
  def list_properties(self):
    self.rating
    self.price
    self.h3_title
    self.li_items
    self.content
    self.link
    self.title

parsed_item = ParsedItem.new(page: ITEM_HTML)
  