# NOTE: 1. Generator = Iterator + Iterable
# 		2. A generator object is a special kind of Iterator object, it is Iterable by design
# 		3. In Order to work with list or FOR loops, a Python Object must be Iterable
#		4. filter/map are generator objects meaning they are both Iterator and Iterable
#		5. A Generator object is not Callable, it cannot be invoked
#		6. We can only call next, and list methods on Generator objects
# 1. Any object in Python which allows/supports next method is an Iterator
# 2. Iterators and Iterable are 2 different types of objects in Python
# 3. An Iterator object supports next method but does not support iterator such as for loop
# 4. An Iterable object supports Iterator as in for loop
# 5. To be an Iterable Object:
#		a. Implement __iter__(self) method
#				OR
#		b. Implement 1. __next__(self) and 2. __getitem__(self, index) methods
# 6. To be an Iterator Object:
#		a. Implement __next__(self) method
# 

# Ways to create a Generator Object
# 	a. Generator Comprehension
#	b. Method which uses yield and current, when invoked returns a Generator object
#		=> The method itself is a simple function but when invoked, it returns a generator object
#		=> Call next on the generator object, not on the method
#		=> g = met() [method invoked returns a generator object]
#		=> next(g)
#		=> list(g)
#	c. Class which implements 
# 		1. __next__(self) method => Raise StopIterationError at the end, this makes it an Iterator
#		2. __iter__(self) method => This makes it an Iterable
#
#  Iterator:
#	a. filter/map: These are generator objects, meaning they are both Iterator and Iterable

#  Iterable:
#	a. An Iterable object supports Iterations, meaning FOR loop, and list methods
#
# If you call list on a generator object, it starts from the last value of the sequence and returns
# all the items

def generator_invoke(generator_call, invoke_list = False, invoke_next = False):
    g = generator_call()
    print(g)
    print(next(g))
    print(next(g))
    print(next(g))
    if invoke_next:
        print(' Invoking __next__')
        print(g.__next__())
    if invoke_list:
        print(list(g))
        # Subsequent invocations of list does not raise StopIterationError, it sees the error and simply returns an empty array
        print(list(g))

def first_hundred():
    i = 0
    while i < 100:
        yield i
        i += 1

# generator_invoke(first_hundred, True)

# Iterator not Generator because it does not support __iter__ method
class FirstHundred():
    def __init__(self):
        self.current = 0
        
    def __next__(self):
        if self.current < 100:
            i = self.current
            self.current += 1
            return i
        else:
            raise StopIteration()

# Generator object

class SecondHundred():
    def __init__(self):
        self.current = 0
    
    def __next__(self):
        if self.current < 100:
            i = self.current
            self.current += 1
            return i
        else:
            raise StopIteration()
        
    def __iter__(self):
        return self

# generator_invoke(FirstHundred, False, True)
# generator_invoke(SecondHundred, True, True)

def starts_with_r(friend: str):
    if friend.startswith('R'):
        return True
    else:
        return False

friends = ['Rolf', 'Joe', 'Black', 'Adam', 'Randy', 'Roe', 'Ross']
my_filter = filter(starts_with_r, friends)
my_filter_2 = filter(lambda friend: friend.startswith('R'), friends)

# print(my_filter)
# print(next(my_filter))
# print(next(my_filter))

# print(my_filter_2)
# print(next(my_filter_2))
# print(next(my_filter_2))

# print('Using for loop with filters')
# for friend in my_filter_2:
#     print(friend)
# print('Using list with filters')
# print(list(my_filter_2))

# A class which implements a generator class has to be invoked to create a generator object
# Similary a method which implements an Iterator functionality has to be invoked to create a generator object
# However, a filter or a custom filter (defined through a function) returns a generator object by itself and
# does not have to be invoked
# A generator object is not callable, it cannot be invoked
# We can only use next, or list on a generator object
# So, my_filter_3() will not work
def my_custom_filter(func, iterable):
    for x in iterable:
        if func(x):
            yield x
my_filter_3 = my_custom_filter(lambda friend: friend.startswith('R'), friends)

# print(next(my_filter_3))
# print(list(my_filter_3))

# A generator comprehension which creates a filter function, a little more
# complex because it uses comprehension with conditional
my_filter_4 = (friend for friend in friends if friend.startswith('R'))

# print(next(my_filter_4))
# print(next(my_filter_4))

# Because a filter object is a generator object, both for loop and list
# functions can be called on it
# for friend in my_filter_4:
#     print(friend)

# print(list(my_filter_4))

friends_lower = map(lambda friend: friend.lower(), friends)

# print(next(friends_lower))
# print(next(friends_lower))

# for friend in friends_lower:
#     print(friend)
    
# print(list(friends_lower))

# Generator comprehension which achieves the same function as map
friends_lower_2 = (friend.lower() for friend in friends)

# print(next(friends_lower_2))
# print(next(friends_lower_2))

# for friend in friends_lower_2:
#     print(friend)
    
# print(list(friends_lower_2))
        
friends_locations = [
	{
		'name': 'Ross',
		'location': 'San Francisco'
	},
	{
		'name': 'Adam',
		'location': 'Austin'
	},
	{
		'name': 'Randy',
		'location': 'Los Angeles'
	}
]
location = input('Enter your location :: ')
nearby_friends = [friend for friend in friends_locations if friend['location'].lower() == location.lower()]

# any returns true if for even 1 element in the list, True is returned
# it calls bool function on each element of the list
# Values for which bool returns False:
#	a. 0, 0.0
# 	b. [], (), {}
#	c. False
# 	d. None
if any(nearby_friends):
    print(f'Nearby Friends :: {nearby_friends}')
    
# all returns True if for all elements in the list, True is returned
x = [0, 1, 2, ['a'], True]
y = [1, 2, True, ['b']]

if all(x):
    print(x)
    
if all(y):
    print(y)