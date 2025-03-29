
def create_file(file_name):
  with(open(file_name, 'w')) as file:
    pass

def _process_file_as_arr(file_data):
  books = []
  for data in file_data:
    file_data_split = data.split(',')
    books.append({ 'name': file_data_split[0], 'author': file_data_split[1], 'read': file_data_split[2] })
  
  return books

def _read_file(file_name):
  file_data = ''
  with(open(file_name, 'r')) as file:
    file_data = [line.strip() for line in file.readlines()]

  return file_data

def _write_to_file(file_data_to_write, file_name):
  with(open(file_name, 'w'))as file:
    file.write(file_data_to_write)

def add_book(book, file_name):
  book_details = f'{book['name']}, {book['author']}, NotRead \n'
  with(open(file_name, 'a')) as file:
    file.write(book_details)
  
  print(' Book added')  
  get_all_books(file_name)
    
def get_all_books(file_name):
  books = _process_file_as_arr(_read_file(file_name))
  print(f' Books :: {books}')
  return books

def mark_book_as_read(book, file_name):
  file_data_to_write = ''
  
  file_data = _read_file(file_name)
  book_found = False

  for data in file_data:
    file_data_split = data.split(',')
    file_data_to_write += f'{file_data_split[0].strip()}, {file_data_split[1].strip()}, '
    if file_data_split[0].lower() == book['name'].lower():
      file_data_to_write += f'Read\n'
      book_found = True
    else:
      file_data_to_write += f'{file_data_split[2].strip()}\n'
      
  _write_to_file(file_data_to_write, file_name)
  if book_found:
    print(' Book Found and marked as read')
  else:
    print(' Book not found')

  get_all_books(file_name)


def delete_book(book, file_name):
  file_data_to_write = ''
  file_data = _read_file(file_name)
  book_found = False
  
  for data in file_data:
    file_data_split = data.split(',')
    if file_data_split[0].lower() == book['name'].lower():
      book_found = True
      next
    else:
      file_data_to_write += f'{data}\n'
      
  if book_found:
    print(' Book found, and deleted')
  else:
    print(' Book not found')

  _write_to_file(file_data_to_write, file_name)
  get_all_books(file_name)
  