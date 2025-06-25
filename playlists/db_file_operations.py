from file_menu_choice import enter_book_info, get_user_choice
from db_books import add_book, mark_book_as_read, delete_book, get_all_books, create_table

user_choice = ''
db_name = 'data.db'

create_table(db_name)

def process_user_choice(user_choice: str):
	if user_choice == 'a':
		book_details = enter_book_info()
		add_book(db_name, book_details)
	elif user_choice == 'b':
		get_all_books(db_name)
	elif user_choice == 'c':
		book_details = enter_book_info()
		mark_book_as_read(db_name, book_details)
	elif user_choice == 'd':
		book_details = enter_book_info()
		delete_book(db_name, book_details)
	else:
		print(' Have a good day!')
  
   
  
while user_choice != 'e':
  user_choice = get_user_choice()
  process_user_choice(user_choice)
