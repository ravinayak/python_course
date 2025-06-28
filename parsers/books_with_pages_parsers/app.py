from parsers.books_with_pages_parsers.pages.all_pages import AllPages
from parsers.books_with_pages_parsers.parsers.book_parser import BookParser
from parsers.books_with_pages_parsers.parsers.all_books_parser import AllBooksParser
from typing import List

URL_TEMPLATE = 'https://books.toscrape.com/catalogue/page-{}.html'
BOOK_URL = 'https://books.toscrape.com/'
RATING_MAP = {
	'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5
}

TOTAL_PAGES = AllPages(url = BOOK_URL).total_pages
PAGE_GEN = (page_num for page_num in range(TOTAL_PAGES))

def menu():
    return (
        f'\n\n **** MENU ****\n\n'
        f' Please enter from one of the choices below: \n'
		f' a. Find 5 cheapest books on the page \n'
		f' b. Find the 5 most highly rated books on the page \n'
		f' c. Find Books on the next page \n'
		f' d. Exit \n\n'
		f'*****************\n\n'
		f' Please enter your choice :: '
	)

def cheapest(books: List[BookParser]):
    five_cheapest_books = sorted(books, key = lambda book: book.price)[:5]
    for index, book in enumerate(five_cheapest_books, start = 1):
        print(f'{index}. {book}')
    return five_cheapest_books
    
def rated(books: List[BookParser]):
    five_highest_rated = sorted(books, key = lambda book: RATING_MAP.get(book.rating, 1), reverse = True)[:5]
    for index, book in enumerate(five_highest_rated, start = 1):
        print(f'{index}. {book}')
    return five_highest_rated

def next_books():
    current_page = next(PAGE_GEN) + 1
    print(f' \n\n**************** Books on Page {current_page} ****************\n\n')
    books = AllBooksParser(url = URL_TEMPLATE.format(current_page + 1)).books
    print(books, end = "\n\n")
    return books
    
FUNCTION_DICT = {
	'a': lambda books: cheapest(books),
	'b': lambda books: rated(books),
}


def run():
    books = next_books()
    user_choice = ''
    while user_choice != 'd':
        print(menu(), end = "")
        user_choice = input()
        if user_choice in ['a', 'b']:
            FUNCTION_DICT[user_choice](books)
        elif user_choice == 'c':
            books = next_books()
    
run()