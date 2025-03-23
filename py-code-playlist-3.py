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

class NoGradeError(Exception):
	pass

class RisingStudent:
  def __init__(self, name):
    self.name = name
    self.grades = []
    
  def add_grade(self, grade):
    raise NotImplementedError("This method is not yet implemented")
  
  def average_grade(self, grades_arr):
    # if len(self.grades) == 0:
    #   raise ValueError("There are no grades yet")
    if not isinstance(grades_arr, list):
      raise NoGradeError("Grades should be a list")
  
    return sum(self.grades) / len(self.grades)
  
rising_student = RisingStudent('Rolf')
print(f"Rising Student :: {rising_student.name} -- {rising_student.grades}")

try:
  print(f"Add Grade :: {rising_student.add_grade(10)}")
except NotImplementedError:
  print("Method not yet implemented")

print(f"Average Grade :: {rising_student.average_grade((2, 3))}")
 