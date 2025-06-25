from file_menu_choice import enter_book_info, get_user_choice
from csv_file_books import create_file, add_book, get_all_books, delete_book, mark_book_as_read

# Part of Playlist 7+8+9

user_choice = ''
file_name = 'books.csv'

create_file(file_name)

def process_user_choice(user_choice):
  if user_choice == 'a':
    book_details = enter_book_info()
    add_book(book_details, file_name)
  elif user_choice == 'b':
    get_all_books(file_name, True)
  elif user_choice == 'c':
    book_details = enter_book_info()
    mark_book_as_read(book_details, file_name)
  elif user_choice == 'd':
    book_details = enter_book_info()
    delete_book(book_details, file_name)
  else:
    print('Have a nice day!')

while user_choice != 'e':
	user_choice = get_user_choice()
	process_user_choice(user_choice)