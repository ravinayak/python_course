# We have 2 types of numbers in Python - a. Integers (Whole Numbers) b. Float
# "#" symbol can be used to write a comment
# Maths works as normal, BODMAS applies

# age = 30
# print(age)
# age = 40
# print(age)

friend_age = 90
print(friend_age)

# age = 35 # integer
# PI = 3.14159 # float

# maths_operations = 1 + 3 * 4 / 2 -2 
# print(maths_operations)

# float_division = 12 / 3
# print(float_division)

# integer_division = 12 // 3 # Remove everything after decimal
# print(integer_division)

# float_division_1 = 8 / 3
# print(float_division_1)

# integer_division_1 = 8 // 3 # Does not round, removes everyting after decimal
# print(integer_division_1)

# remainder = 13 % 5
# print(remainder)

# my_string = "Hello World!"
# print(my_string)

# string_with_multiple_quotes = "Hello! It's a wonderful day"
# print(string_with_multiple_quotes)

# str_with_escape = "Hello! It\"s a wonderful day"
# print(str_with_escape)

# multiline_str = """Hello World

# This file is going to be printed
# """
# print(multiline_str)

# """
# Strings like these in python
# programs are not treated as variables
# They are simply left out of the program
# like comments
# """
# name = 'Joe'
# concat_str = 'Hello World ' + name
# print(concat_str)

# age = 34
# """
# In Python we cannot add different data types
# to concatenate them, they must be of the
# same data type
# To perform concatenation, both data types
# must be strings
# """
# age = "34"
# your_age = "Your age " + age
# print(your_age)
# age_1 = 34
# your_age_1 = "Your age " + str(age)
# print(your_age_1)

# # Variable Interpolation
# age = 34
# greeting = f"Your age is {age}"
# print(greeting)
# age = 35
# # Even if we change the value of age, greeting retains its value of age as 34 because this was the 
# # value which was used for computing greeting
# print(greeting)

# # If we want to interpolate variables dynamically, we should use format option
# final_greeting = "How are you, {}?"
# name = 'Jose'
# print(final_greeting.format(name))
# name = 'Bye'
# print(final_greeting.format(name))

# # Variable Replacement, Python looks for name variable and replaces it with the given value
# greet = "How are you {name}?"
# print(greet.format(name='Rahul'))
# name = 'Raj'
# # name is the variable in curly braces, and 2nd name is the variable defined outside
# print(greet.format(name=name))

# # Taking input from user - user input is always a string
# age = input("Enter your age :: ")
# print(f"You have lived for {12 * age} months")

# # Multiplying a string by a number concatenates string that many times
# # "12" + "3" = "123" just like "Ra" + "hul" => "Rahul"
# # "12" + "3" + "3" = "1233"
# # "12" * "4" = "12121212" = "12" + "12" + "12" + "12"
# age_int = int(age)
# age_int_1 = int(input("Enter your age :: "))
# print(f"You have lived for {12 * age_int_1} months")

# my_number = 5
# age = 20
# age_over_18 = age >= 18
# age_under_18 = age < 18
# print(f"Over Age :: {age_over_18}")
# print(f"Under Age :: {age_under_18}")

# user_number = int(input("Enter your number :: "))
# print(f"You got it right :: {my_number == user_number}")

# friends = ['Rahul', 'Raj', 'Shilpa']
# print(friends[0])
# print(friends)
# # print(friends.remove('Not'))
# friends = [['Raj', 1], ['Rahul', 2], ['Kal', 3]]
# print(friends[0])
# print(friends)
# print(friends.remove(['Raj', 1]))
# print(friends)
# print(friends.append(['Tomorrow', 4]))
# print(friends)

# Tuples can be written without brackets, but it can get confusing especially when we use it inside a list
# Hence prefer using brackets always with tuples
# Tuples are static, and cannot be modified, when we add or remove an element from a tuple, it creates a new tuple
# Lists on the other hand can be modified, elements can be added/removed from a list
# tuples = ("Raj", "Rahul")
# print(tuples)
# # If you forget a comma after 'Kiran', it will be considered as a string and not a tuple
# # Python will give a TypeError and not add the str to tuple
# tuples = tuples + ('Kiran',)
# print(tuples)

# set_elements = { 'Freddy', 'Thomas' }
# set_elements.add('Jane')
# print(set_elements)
# set_elements.add('Jane')
# print(set_elements)
# set_elements.remove('Jane')
# print(set_elements)

# art_friends = { "Rolf", "Jen", "Anne"}
# science_friends = { "Jen", "Charlie"}

# art_but_not_science = art_friends.difference(science_friends)
# print(art_but_not_science)
# science_but_not_art = science_friends.difference(art_friends)
# print(science_but_not_art)
# not_in_both_science_art = art_friends.symmetric_difference(science_friends)
# print(not_in_both_science_art)
# intersection_art_science = art_friends.intersection(science_friends)
# print(intersection_art_science)
# union_art_science = art_friends.union(science_friends)
# print(union_art_science)
# friends_ages = { "Rolf": 24, "Adam": 30, "Anne": 27 }
# print(friends_ages["Rolf"])
# print(friends_ages)
# friends = (
# 	{ "Rolf": 24, "Adam": 30},
# 	{ "Key" : 35, "Value": 45}
# )
# print(friends[0]["Rolf"])
# friends = [("Rolf", 24), ("Adam", 30), ("Anne", 27)]
# print(dict(friends))
grades = [80, 75, 90, 100]
total = sum(grades)
length = len(grades)
print(total)
print(length)