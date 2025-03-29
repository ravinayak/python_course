from csv_books import add_book, get_all_books, delete_book, mark_book_as_read

books_menu = '''Available Options:
a. Add a book
b. Get all books
c. Mark a book as read
d. Delete a book
e. Quit
'''

user_choice = ''

def get_user_choice():
  print('\n')
  print(books_menu)
  incorrect_choice = True
  while incorrect_choice:
    user_choice = input(' Please Enter your choice :: ')
    for menu_option in ['a', 'b', 'c', 'd', 'e']:
      if menu_option == user_choice:
        incorrect_choice = False
  return user_choice
  
def enter_book_info():
  book_name = input(' Please Enter book name :: ')
  book_author = input(' Please Enter book author :: ')
  return { 'name': book_name, 'author': book_author }

def process_user_choice(user_choice):
  if user_choice == 'a':
    book_details = enter_book_info()
    add_book(book_details)
  elif user_choice == 'b':
    get_all_books()
  elif user_choice == 'c':
    book_details = enter_book_info()
    mark_book_as_read(book_details)
  elif user_choice == 'd':
    book_details = enter_book_info()
    delete_book(book_details)
  else:
    print('Have a nice day!')

while user_choice != 'e':
	user_choice = get_user_choice()
	process_user_choice(user_choice)