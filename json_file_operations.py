from json_file_books import add_book, mark_book_as_read, delete_book, get_all_books, create_file
from file_menu_choice import get_user_choice, enter_book_info

user_choice = ''
file_name = 'books.json'
create_file(file_name)

def process_user_choice(user_choice):
  if user_choice == 'a':
    book_details = enter_book_info()
    add_book(book_details, file_name)
  elif user_choice == 'b':
    get_all_books(file_name)
  elif user_choice == 'c':
    book_details = enter_book_info()
    mark_book_as_read(book_details, file_name)
  elif user_choice == 'd':
    book_details = enter_book_info()
    delete_book(book_details, file_name)
  else:
    print('Have a good day!')

while user_choice != 'e':
	user_choice = get_user_choice()
	process_user_choice(user_choice)