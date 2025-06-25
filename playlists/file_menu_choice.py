books_menu = '''Available Options:
a. Add a book
b. Get all books
c. Mark a book as read
d. Delete a book
e. Quit
'''

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