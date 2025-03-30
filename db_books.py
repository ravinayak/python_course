import sqlite3
from database_connection import DatabaseConnection

def create_table(db_name):
  with(DatabaseConnection(db_name)) as connection:
    cursor = connection.cursor()

    cursor.execute('Create table IF NOT EXISTS books(name text primary key, author text, read integer)')
    
  return None
    
def get_all_books(db_name):
  with(DatabaseConnection(db_name)) as connection:
    cursor = connection.cursor()

    cursor.execute('Select * from books;')

    print(' Retrieved all books')
    books = [
      { 'name': row[0], 'author': row[1], 'read': 'Read' if row[2] == 1 else 'NotRead' }
    	for row in cursor.fetchall()
		]
  
  print(f' Books :: {books}')
  return books

def add_book(db_name, book):
  with(DatabaseConnection(db_name)) as connection:
    cursor = connection.cursor()
    try:
      cursor.execute('Insert into books VALUES(?, ?, ?)', (book['name'], book['author'], 0))
      print(f' Inserted into books table :: {book}')
    except sqlite3.IntegrityError as e:
      print(f' Exception :: {e}')
      print(' Insertion failed')
    except Exception as e:
      print(f' Error :: {e}')
      print(' Insertion failed')

  get_all_books
  
def mark_book_as_read(db_name, book):
  with(DatabaseConnection(db_name)) as connection:
    cursor = connection.cursor()

    cursor.execute('Update books set read = 1 where name=(?)', (book['name'],))
    cursor.execute('Select * from books where name=(?)', (book['name'],))
    print(f" Marked book as read :: {book['name']}")

  get_all_books

def delete_book(db_name, book):
  print(f' Deleting book :: {book}')
  with(DatabaseConnection(db_name)) as connection:
    cursor = connection.cursor()

    cursor.execute('Delete from books where name=(?)', (book['name'],))
    print(f" Deleted book :: {book['name']}")
    
  get_all_books