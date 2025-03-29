
def create_file(file_name):
  with(open(file_name, 'w')) as file:
    pass

def _process_file(file_name):
  file_data = ''
  with(open(file_name, 'r')) as file:
    file_data = [line.strip().split(',') for line in file.readlines()]
  return [
		{ 'name': file_data_split[0].strip(), 'author': file_data_split[1].strip(), 'read': file_data_split[2].strip()}
		for file_data_split in file_data
	]

def _save_to_file(books, file_name):
  with(open(file_name, 'w')) as file:
    for book in books:
      file.write(f'{book['name']}, {book['author']}, {book['read']}\n')

def print_books(file_name):
  books = get_all_books(file_name)
  print(f' Books :: {books}')

def add_book(book, file_name):
  book_details = f'{book['name']}, {book['author']}, NotRead \n'
  with(open(file_name, 'a')) as file:
    file.write(book_details)
  
  print(' Book added')  
  print_books(file_name)
    
def get_all_books(file_name, print_books = False):
  books = _process_file(file_name)
  if print_books:
    print(f' Books :: {books}')
  return books

def mark_book_as_read(book, file_name):  
  books = get_all_books(file_name)
  book_found = False

  for list_book in books:
    if list_book['name'].lower() == book['name'].lower():
      list_book['read'] = 'Read'
      book_found = True
    
  _save_to_file(books, file_name)
  if book_found:
    print(' Book Found and marked as read')
  else:
    print(' Book not found')
  
  print_books(file_name)


def delete_book(book, file_name):
  books = get_all_books(file_name)
  book_found = False
  
  for list_book in books:
    if list_book['name'].lower() == book['name'].lower():
      books.remove(list_book)
    else:
      next
      
  if book_found:
    print(' Book found, and deleted')
  else:
    print(' Book not found')

  _save_to_file(books, file_name)
  print_books(file_name)
  