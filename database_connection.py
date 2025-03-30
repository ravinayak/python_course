import sqlite3

class DatabaseConnection:
  def __init__(self, db_name):
    self.connection = None
    self.db_name = db_name
    
  def __enter__(self):
    self.connection = sqlite3.connect(self.db_name)
    return self.connection
    
  def __exit__(self, exec_type, exec_val, exec_tb):
    try:
      if exec_type or exec_val or exec_val:
       print(f' Exception in database connection :: Type -- {exec_type}, Value -- {exec_val}, Traceback -- {exec_tb}')
       self.connection.close()

      self.connection.commit()
      self.connection.close()
    except sqlite3.OperationalError as e:
      print(f'Exception - Operational :: {e.with_traceback}')
    except Exception as e:
    	print('Exception caught')