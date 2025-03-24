import json

dict = {
	'name': 'Joe',
	'grades': [10, 20, 30, 20, 20],
  'average': lambda grades: sum(grades) / len(grades)
}

# print(dict['name'])
# print(dict['grades'])
# print(dict['average'](dict['grades']))
# print(dict['average'])

class Student:
  def __init__(self, name, grades):
    self.name = name
    self.grades = grades
    self.average = 0
    
  def average_grade(self):
    average = sum(self.grades) / len(self.grades)
    print(f"Average Grade :: {average}")
    return average

# student = Student('Rolf', [10, 20, 30, 20, 20])
# print(student.name)
# student.average_grade()

class WorkingStudent(Student):
  def __init__(self, name, grades):
    super().__init__(name, grades)
    self.hourly_rate = 125 # per hour
    
  def total_weekly_salary(self):
    return self.hourly_rate * 40 * 7
  
  def set_average(self, new_average):
    self.average = new_average
    return self.average
  
# working_student = WorkingStudent(name='Rolf', grades = [10, 20, 30, 20, 20])
# print(working_student.name)
# print(working_student.hourly_rate)
# print(working_student.total_weekly_salary())
# print(working_student.average_grade())
# print(working_student.__class__.__name__)
# print(working_student.average)
# print(working_student.set_average(150))

dict = {
	'name': 'Joe',
  'grades': [10, 20, 30, 20, 20],
  'average': lambda grades: sum(grades) / len(grades)
}

# print(dict['name'])
# print(dict['grades'])
# print(dict['average'](dict['grades']))

class Car:
  def __init__(self, make, model):
    self.make = make
    self.model = model
  
  def __repr__(self):
   return f"This car is {self.make} -- {self.model}"
 
  def __str__(self):
   return f"Car - Make :: {self.make}, Model :: {self.model}"

car = Car('Ford', 'Fiesta')
# print(car)
# print(str(car))

class Garage:
  def __init__(self):
    self.cars = []
    
  def __len__(self):
    return len(self.cars)
  
  def __getitem__(self, i):
    return self.cars[i]
  
  def add_car(self, car):
    if not isinstance(car, Car):
      raise TypeError(f"Only car objects can be added to Garage, not {car.__class__.__name__}")
    self.cars.append(car)

garage = Garage()
# print(len(garage))

# try:
#   garage.add_car('Ford')
# except TypeError:
# 	print("Your car was not a Car object")
  
try:
	garage.add_car(car)
except TypeError:
	print("Your car was not a Car object")
  
# print(garage[0])

tesla_car = Car('Tesla', 'Model Y')
Garage.add_car(garage, tesla_car)
# print(garage[1])

class Hero:
  def __init__(self, name, age = 25, height = 6):
    self.name = name
    self.age = age
    self.height = height
    
  def __repr__(self):
    return f"Hero Attributes :: Name :: {self.name}, Age :: {self.age}, Height :: {self.height}"
  
hero_one = Hero('Without Arguments')
hero_two = Hero('With Only 1 Argument', age = 30)
hero_three = Hero('With All Arguments', age = 35, height = 7)
# print(hero_one)
# print(hero_two)
# print(hero_three)

class WorkingClass:
  def __init__(self, hourly_rate = 25):
    self.hourly_rate = hourly_rate
    
  @property
  def weekly_salary(self):
    return self.hourly_rate * 40
  
working_class = WorkingClass(30)
# print(working_class.weekly_salary)
# Since weekly_salary is a property, it CANNOT be called as a method => print(working_class.weekly_salary())

class FixedFloat:
  def __init__(self, amount = 25):
    self.amount = amount
    
  def __repr__(self):
    return f'Fixed Float :: {self.amount:.2f}'
  
  @classmethod
  def to_amount(cls, value):
    return cls(value)
  
  @staticmethod
  def from_sum(value1, value2):
    return f'This calculates the total value :: {(value1 + value2)}'
  
class Euro(FixedFloat):
  def __init__(self, amount = 45):
    super().__init__(amount)
    self.symbol = '€'
    
  def __repr__(self):
    return f'Euro :: {self.symbol} {self.amount:.2f}'

# print(Euro(35))
# print(Euro.to_amount(35))
# print(Euro.from_sum(35, 45))

class MyCustomError(TypeError):
  '''
    This is a custom error I am creating
  '''
  def __init__(self, message, code):
    super().__init__(f'This is MyCustomError :: {message} :: {code}')
    self.code = code
  
error = MyCustomError('Error', 500)

# print(error.__doc__)

# raise error

class ApartmentError(Exception):
  def __init__(self, message, code):
    super().__init__(f"Apartment Error Custom :: {message} -- {code}")
    self.code = code
class Apartment:
  def __init__(self, name, rent):
    self.name = name
    self.rent = rent
    self.apartments = []
    
  def add_apartment(self, apartment):
    if isinstance(apartment, str):
      raise TypeError('A String was passed instead of an Apartment object', 400)
    if not isinstance(apartment, Apartment):
      raise ApartmentError('This is not an Apartment object', 400)
    self.apartments.append(apartment)
    # print(f'{apartment} added successfully')
    
  def __repr__(self):
    return f'Apartment :: {self.name} -- {self.rent}'
    
try:
  apartment = Apartment('Apartment - 2', 5000)
  apt = Apartment('Apartment - 1', 2000)
  apartment.add_apartment(apt)
  # apartment.add_apartment('Apartment')
  # apartment.add_apartment(500)
except ApartmentError as e:
  # print('An Apartment Error Occurred')
  raise
except TypeError as e:
  # print('A TypeError occurred')
  raise
else:
  x = 5
  # print('No Exception was Raised')
finally:
  x = 2
  # print('This statement is always executed')
  
class DoubleSquare:
  
  # Error because user_input is a string and cannot be parsed to float
  def square_one(self):
    user_input = float(input('Enter a number :: '))
    n = user_input * user_input
    return n
  
  # Error: NameError
  # Error because n is defined within try block and hence
  # not in the scope of except block, when an error occurs
  # n remains undefined => NameError when user inputs a string
  def square_two(self):
    try:
      user_input = float(input('Enter a number :: '))
      n = user_input * user_input
      return n
    except ValueError:
      return n
  
  # No Error
  # Works because if error occurs, it goes into except block
  # and n is defined there before executing finally block
  def square_three(self):
    try:
      user_input = float(input('Enter a number :: '))
      n = user_input * user_input
      return n
    except ValueError:
      n = 0
      return n
    finally:
      print(f'Finally block executed :: {n}')
    
  # Error occurs because when user inputs a string, it raises
  # an error and n remains undefined. Finally block is executed
  # but n is not defined => NameError
  def square_four(self):
    try:
      user_input = float(input('Enter a number :: '))
      n = user_input * user_input
    except ValueError:
      return 0
    finally:
      return n
  
  # No Error
  # Works because n is defined in the try block and when error occurs
  # 0 is returned, else block is not executed. Else block is executed
  # when No Error occurs, and in this case, n is defined
  def square_five(self):
    try:
      user_input = float(input('Enter a number :: '))
      n = user_input * user_input
      print('f User Input worked :: {n}')
    except ValueError:
      return 0
    else:
      return n
    
double_square = DoubleSquare()
# print(double_square.square_one())
# print(double_square.square_two())
# print(double_square.square_three())
# print(double_square.square_four())
# print(double_square.square_five())

friends_names = ['Rolf', 'Jose', 'Randy', 'Anna']

def write_file(hello = 'Hello'):
  file = open('data.txt', 'w')
  if hello == 'Hello':
    file.write('Hello, World!')
  else:
    for friend_name in friends_names:
      file.write(friend_name + '\n')
  file.close()

def read_file():
  file = open('data.txt', 'r')
  lines = file.readlines()
  file.close()

  lines = [line.strip() for line in lines]
  # print(f'Lines :: {lines}')

write_file(hello = 'Hello')
read_file()
write_file(hello = 'Non')
read_file()

def read_csv():
  file = open('data.csv', 'r')
  lines = file.readlines()
  file.close()
  
  csv_lines = [line.strip().split(',') for line in lines]
  for csv_line in csv_lines:
    for line in csv_line:
      if line != '':
        print(line.strip())
  
def write_csv():
  file = open('data.csv', 'w')
  friends = ['Rolf', 'Jose', 'Randy', 'Anna']
  enemies = ['Jen', 'Sara', 'Randy']
  for enemy in enemies:
    file.write(f'{enemy}, ')
  file.write('\n')
  for friend in friends:
    file.write(f'{friend}, ')
  file.close()
  
# write_csv()
# read_csv()

def read_context_manager_csv():
  with open('data.csv', 'r') as file:
    lines = file.readlines()
    
  print(' \nI am in read context manager \n')

  csv_lines = [line.strip().split(',') for line in lines]
  for csv_line in csv_lines:
    for line in csv_line:
      if line != '':
        print(line.strip())
        
def write_context_manager_csv():
  with open('data.csv', 'w') as file:
    friends = ['Rolf', 'Jose', 'Randy', 'Anna']
    enemies = ['Jen', 'Sara', 'Randy']
    for enemy in enemies:
      file.write(f'{enemy}, ')
    file.write('\n')
    for friend in friends:
      file.write(f'{friend}, ')
      
# write_context_manager_csv()
# read_context_manager_csv()

def write_json():
  friends = ['Joe', 'Randy', 'Black']
  dict = {
    'friends': [
      {
        'name': 'Joe',
        'age': 25,
      },
      {
        'name': 'Randy',
        'age': 30,
      },
      {
        'name': 'Black',
        'age': 35,
      }
    ]
  }
  with open('data.json', 'w') as file:
    # json.dump(friends, file)
    json.dump(dict, file)
    
def read_json():
  with open('data.json', 'r') as file:
    print(json.load(file))
    
# write_json()
# read_json()

class SerializableObject:
  def __init__(self, rate, amount):
    self.rate = rate
    self.amount = amount

  def to_dict(self):
    return { "object": { "rate": self.rate, "amount" : self.amount } }

def write_string_json():
  friends = '{"friends": {"name": "Joe", "age": 25}}'
  serializable_object =  SerializableObject(25, 50).to_dict()
  print(serializable_object)
  print(json.dumps(serializable_object))
  with open('data_str.json', 'w') as file:
    json.dump(friends, file, indent=2)
    
def read_string_json():
  friends = {}
  with open('data_str.json', 'r') as file:
    friends = json.load(file)
    print(friends)
  print(friends.__class__)
  friends_str = '{"friends": {"name": "Black", "age": 50}}'
  print(json.loads(friends_str))
    
# write_string_json()
# read_string_json()