from bs4 import BeautifulSoup

H1_TAG = 'h1'
SUBTITLE_TAG = 'p.subtitle'
LIST_TAG = 'ul'
LIST_ITEM_TAG = 'li'
LI_TAGS = 'ul li'

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet. Consectetur edipiscim elit.</p>
<p>Here's another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')

def find_h1():
  h1_tag = simple_soup.select_one(H1_TAG)
  print(h1_tag.string)
  
def find_subtitle():
  subtitle_tag = simple_soup.select_one(SUBTITLE_TAG)
  print(subtitle_tag.string)

def find_subtitle_using_class():
  subtitle_tag = simple_soup.select_one('p', { 'class': 'subtitle' })
  print(subtitle_tag.string) 
  
def find_list_items():
  list_items = simple_soup.select(LI_TAGS)
  items = simple_soup.select(LIST_ITEM_TAG)
  items_val = [item.string for item in items]
  print(items_val)
  list_contents = [list_item.string for list_item in list_items]
  print(list_contents)

find_h1()
find_subtitle()
find_subtitle_using_class()
find_list_items()