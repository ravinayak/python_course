import json

def create_file(file_name):
  json_obj = []
  with(open(file_name, 'w')) as file:
    json.dump(json_obj, file)
  
def _read_file(file_name):
  with(open(file_name, 'r')) as file:
    json_obj = json.load(file)
  return json_obj

def _save_to_file(books, file_name):
  with(open(file_name, 'w')) as file:
    json.dump(books, file)

def add_book(book_details, file_name):
  book_details['read'] = 'NotRead'
  books = _read_file(file_name)
  books.append(book_details)
  _save_to_file(books, file_name)
  print(' Book added succesfully')
  get_all_books(file_name)
  
def get_all_books(file_name):
  books = _read_file(file_name)
  print(f' Books :: {books}')

def compare_list_book(list_book, book_details):
  return list_book['name'].lower() == book_details['name'].lower()

def mark_book_as_read(book_details, file_name):
  books = _read_file(file_name)
  book_found = False
  for list_book in books:
    if compare_list_book(list_book, book_details):
      list_book['read'] = 'Read'
      book_found = True
  if book_found:
    print(' Book found and marked as read, saving')
    _save_to_file(books, file_name)
    get_all_books(file_name)
  else:
    print(' Book not found')
  
def delete_book(book_details, file_name):
  books = _read_file(file_name)
  book_found = False
  for list_book in books:
    if compare_list_book(list_book, book_details):
      books.remove(list_book)
      book_found = True
  if book_found:
    print(' Book found and deleted, saving books')
    _save_to_file(books, file_name)
    get_all_books(file_name)
  else:
    print(' Book not found')