import requests
import asyncio
from practice.book_locators_async.all_books.all_books_objects import AllBooksObjects
import practice.book_locators_async.config as Config

async def menu():
	page_content = requests.get(Config.URL).text
	all_books_obj = AllBooksObjects(page_content)

	page_num = all_books_obj.parse_page_num()
	user_input = input('Enter range of page numbers to retrieve all the books for those pages between - 1 and {} :: '.format(page_num))
	input_page = int(user_input)
	
	if input_page < 0 or input_page > page_num:
		print('Invalid Choice, Please enter a number between 1 and {}'.format(page_num))
		print(f'\n\n')
		exit(1)

	input_choice = int(input(Config.MENU_CHOICE))
	print(f'\n\n')
	await process_user_input(input_page, input_choice, all_books_obj)
	
def display_book(str_text, book_dicts):
    print(f'{str_text} :: \n')
    for book_dict in book_dicts:
        print(book_dict)
    
def process_cheapest_books(book_parsers):
    prices = []
    for book_parser in book_parsers:
        prices.append({ 'price': book_parser.price, 'name': book_parser.title } )
    
    cheapest_books = sorted(prices, key=lambda x: x['price'])[0:5]
    display_book('5 Cheapest Books', cheapest_books)
    
    return cheapest_books
    
def process_highest_rated_books(book_parsers):
    rated_books = []
    for book_parser in book_parsers:
        rated_books.append({ 'rating': book_parser.star_rating, 'name': book_parser.title } )
    
    most_rated_books = sorted(rated_books, key=lambda x: x['rating'], reverse=True)[0:5]
    display_book('5 most highly rated books', most_rated_books)

    return most_rated_books
    
def process_book_names_stock_avail(book_parsers):
    book_names_stock_avail = []
    for book_parser in book_parsers:
        book_names_stock_avail.append({ 'name' : book_parser.title, 'in_out_stock': book_parser.stock_avail})
    
    display_book('Book Names and their Stock Availability', book_names_stock_avail)

    return book_names_stock_avail
    
async def process_user_input(input_page_num, input_choice, all_books_obj):
	all_books_parsers = await all_books_obj.process_pages(input_page_num)
	book_parsers = []
	for all_book_parser in all_books_parsers:
		book_parsers.extend(all_book_parser.parse_books())
		
	if(input_choice == 1):
		process_cheapest_books(book_parsers)
	elif(input_choice == 2):
		process_highest_rated_books(book_parsers)
	elif(input_choice == 3):
		process_book_names_stock_avail(book_parsers)
	else:
		print('Please enter a valid choice next time! Thank You!')
	
	print(f'\n\n')
     
	

if __name__ == '__main__':
	asyncio.run(menu())

