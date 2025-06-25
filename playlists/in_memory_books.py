
books = []

def add_book(book):
  print(f' Books before appending :: {books}')
  book['read'] = False
  books.append(book)
  print(f' Books after appending :: {books}')
  
def get_all_books():
  print(f' Books :: {books}')
  return books

def mark_book_as_read(book):
  print(f' Book before being marked as read :: {book}')
  for list_book in books:
    if book['name'].lower() == list_book['name'].lower():
      list_book['read'] = True
  for list_book in books:
    if list_book['name'].lower() == book['name'].lower():
      marked_book = list_book
      print(f' Book after being marked as read :: {marked_book}')
      return marked_book
  print(' Book could not be found, no book marked as read')
  return ''
  
  
def delete_book(book):
  print(f' Books before deleting a book :: {books}')
  book_to_delete = ''
  for list_book in books:
    if list_book['name'].lower() == book['name'].lower():
      books.remove(list_book)
      print(f' Books after deleting book :: {books}')
      return
  print(' Book could not be found, no book deleted')
  return ''