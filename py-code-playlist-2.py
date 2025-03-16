# user_name = input("Enter your name :: ")

# user_higher_learning = input("Are you interested in higher learning? (yes/no) :: ")
# user_lower_learning = input('Are you interested in lower learning? (yes/no) :: ')

# higher_learning = user_higher_learning.lower() == 'yes'
# lower_learning = user_lower_learning.lower() == 'yes'

# if higher_learning:
# 	print(f"{user_name} is interested in higher learning")
# elif lower_learning:
#   print(f"{user_name} is interested in lower learning")
# else:
#   print(f"{user_name} is not interested in learning")

# high_learning = True
# user = input("Enter your name :: ")
# while high_learning:
#   print(f"{user} is interested in high learning")
#   user_learning = input('Are you interested in learning? (yes/no) :: ')
#   high_learning = user_learning.lower() == 'yes'
  
# friends = ['Roe', 'Raj', 'Rohan']

# for friend in friends:
#   print(friend)

# friends = ['Roe', 'Raj', 'Rohan']
# user_name = input("Enter your name :: ")

# for friend in friends:
#   if friend.lower() == user_name.lower():
#     print(f"{user_name} is your friend")
#     break

# car_manufacturing = ['yes', 'yes', 'yes', 'no', 'yes']

# Naive way to find if all cars were manufactured
# all_cars_manufactured = True

# for car_manufactured in car_manufacturing:
#   if car_manufactured.lower() == 'no':
#     all_cars_manufactured = False
#     break

# if all_cars_manufactured:
#   print("All cars were manufactured")
# else:
#   print('All cars were not manufactured')

# car_manufacturing = ['yes', 'yes', 'yes', 'yes', 'yes']

# for car_manufactured in car_manufacturing:
#   if car_manufactured.lower() == 'no':
#     print("All cars were not manufactured")
#     break
# else:
#   print('All cars were manufactured')

# usd, eur = 1, 0.85
# print(f"usd :: {usd}, eur :: {eur} is an example of Destructuring Syntax")

# tuples_list = [('Roe', 12), ('Raj', 13), ('Rohan', 14)]

# for name, age in tuples_list:
#   print(f"{name} is {age} years old")

# print("\n")
# dict_items = { 'Roe': 12, 'Raj': 13, 'Rohan': 14 }

# for name in dict_items:
#   print(f"{name} is in dict_items")
  
# for age in dict_items.values():
#   print(f"{age} is in dict_items")

# for name, age in dict_items.items():
#   print(f"{name} is {age} years old")

# numbers = [1, 2, 3, 4, 5]
# doubled_numbers = []

# for number in numbers:
#   doubled_numbers.append(number * number)
  
# print(f"Doubled Numbers :: {doubled_numbers}")

# doubled_numbers = [number * number for number in numbers]
# print(f"Doubled Numbers :: {doubled_numbers}")

# friends = { 'Roe', 'Raj', 'Rohan' }
# guests = { 'Rohan', 'Vijay', 'Shri Ram', 'Raj' }

# friends_guests = {friend for friend in friends if friend in guests.intersection(friends)}
# print(f"Common Friend in Guests :: {friends_guests}")

# friends_ages = { 'Roe': 12, 'Raj': 13, 'Rohan': 14, 'Vijay': 5, 'Sri': 2, 'Shri Ram': 21 }

# friend_ages_gt_5 = { name: age for name, age in friends_ages.items() if age > 5}
# print(f"Friends with age greater than 5 :: #{friend_ages_gt_5}")

# friends_locations = [('Roe', 'Mumbai'), ('Raj', 'Pune'), ('Rohan', 'Delhi')]
# guests_locations = [('Rohan', 'Delhi'), ('Vijay', 'Mumbai'), ('Shri Ram', 'Pune'), ('Raj', 'Pune')]

# friends_guests_locations = [(friend, location) for friend, location in friends_locations if (friend, location) in guests_locations]

# set_friends_locations = set(friends_locations)
# set_guests_locations = set(guests_locations)
# print(f"Common friends and guests :: #{friends_guests_locations}")
# print(f"Set Intersection :: {set_guests_locations.intersection(set_friends_locations)}")

# for x in range(2, 20):
#   for y in range(2, x):
#     if x % y == 0:
#       print(f"{x} equals {y} * {x/y}")
#       break
#   else:
#     print(f"{x} is a prime number")

# friends_age_dict = { 'Raj': 12, 'Rohan': 13, 'Roe': 14, 'Vijay': 5, 'Sri': 2, 'Shri Ram': 21 }
# friends_age_gt_t = { 
#                     friend: age 
#                     for friend, age in friends_age_dict.items() 
#                     if age > 5
#                     }

# print(f"Friends with age > 5 :: {friends_age_gt_t}")

# friends = ['Roe', 'Raj', 'Rohan', 'Vijay', 'Sri', 'Shri Ram']

# print(f"friends: {friends[1:]}")
# print(f"friends: {friends[1:4]}")
# print(f"friends: {friends[1:6]}")
# print(f"friends: {friends[:]}")
# print(f"friends: {friends[-3:]}")
# print(f"friends: {friends[-3:-1]}")
# print(f"friends: {friends[-2:-1]}")

# friends = ['Roe', 'Raj', 'Rohan', 'Vijay', 'Sri', 'Shri Ram']
# age = [12, 14, 15, 21, 25, 30]

# friends_age = dict(zip(friends, age))
# print(f"friends age hash :: {friends_age}")
# print(f"Zip object :: {zip(friends, age)}")
# print(f"dict with more ages than friends :: {dict(zip(friends, [12, 15, 15, 21, 25, 30, 35, 25]))}")
# print(f"dict with less ages than friends :: {dict(zip(friends, [12, 15, 15, 21]))}")

# friends = ['Roe', 'Raj', 'Rohan', 'Vijay', 'Sri', 'Shri Ram']
# Without enumerate
# index = 0
# for friend in friends:
#   print(f"friend :: {friend}, index :: {index}")
#   index +=1

# for index, friend in enumerate(friends):
#   print(f"friend :: {friend}, index :: {index}")

# def greet():
#   print('Hello World')
  
# hello = greet
# hello()

# def calculate_sum(x, y=20, z=30):
#   print(f"Sum of {x}, {y}, {z} is {x+y+z}")

# calculate_sum(x=5, y=10, z=40)
# calculate_sum(5)
# calculate_sum(5, y=10, z=40)

# def return_val(x):
#   return x * x

# def return_implicit_none(y):
# 	print(f"{y} square is {y * y}")

# def return_explicit_none(z):
#   print(f"{z} square is {z * z}")
#   return None
 
# print(f"return_val(5) :: {return_val(5)}")
# print(f"return_implicit_none(5) :: {return_implicit_none(y=5)}")
# print(f"return_explicit_none(5) :: {return_explicit_none(5)}")

# cars = [
# 	{'make': 'Honda', 'model': 'Civic', 'price': 14000},
#   {'make': 'Toyota', 'model': 'Corolla', 'price': 5000},
#   {'make': 'Ford', 'model': 'Fiesta', 'price': 7000},
#   {'make': 'Afford', 'model': 'Fiesta', 'price': 2000},
# ]

# def average_price(cars):
#    return (sum(car['price'] for car in cars))	/ len(cars)

# def car_with_avg_price(cars):
#   for car in cars:
#     avg_price = int(average_price(cars))
#     if car['price'] == avg_price:
#       return car
#   else:
#     return {'make': 'Unknown', 'model': 'Unknown'}

# def car_model(cars):
#   return car_with_avg_price(cars)['model']

# def car_make(cars):
#   return car_with_avg_price(cars)['make']

# print(f"Average Price :: {average_price(cars)} -- Car Model :: {car_model(cars)} -- Car Make : {car_make(cars)}")

# car_prices = [700, 1000, 2000, 5000]
# max_car_price = lambda sequence: max(sequence)
# sum_of_car_prices = lambda sequence: sum(sequence)

# print(f"Max Car Price :: {max_car_price(car_prices)} -- Sum of Car Prices :: {sum_of_car_prices(car_prices)}")

