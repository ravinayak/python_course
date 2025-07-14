# Calling generator_object.send(None) is used to prime a generator.
# Priming a generator object means executing all lines of code in the
# generator object until it encounters the first yield.
# yield statement is NOT EXECUTED

# CRUCIAL:
#	It is Critical to note that although yield statement is not executed
# if we are yielding a value in that line, such as,
#		yield <value>
# value will be returned to the caller, though yield <value> line has not
# been executed. This line will only be executed on a subsequent call to
# next() or .send()

# This is same as the USE CASE where we would send a Non None value to
# to the generator object. Every time we call "send", it executes all the
# lines of code upto the 1st "yield" and pauses there without executing
# "yield". This behavior is consistent in both the cases where we pass
# None and non None values to the generator object

# Every time you make a subsequent call to next(generator object) or
# generator_object.send(<value>), all lines of code including the "yield"
# statement (where it had paused) and after the "yield" statement are executed.
# until it encounters a "yield" again. The "yield" statement encountered is
# not executed and execution pauses at the "yield" statement

# Every ".send()" or "next()" method called on a generator object corresponds
# to execution of 
# a. All the statements in the generator object until it encounters a yield
# b. "yield" statement is NOT EXECUTED
# c. yield <value> will return value to the caller although the statement is
# not executed. "yield <value>" returning "<value>" to the caller is not the same
# as executing that line
# c. A subsequent statement next() or .send() executes "yield" statement, and
# 	 all the statements after the "yield" until it encounters a "yield" again
# d. Execution pauses at "yield" statement without executing "yield"

def greet():
    while True:
        # Here the greet method receives value passed to it though
        # send method on the greet generator object
        # g.send(None) reaches the following line of execution and
        # pauses at the line, it does not execute yield
        name = yield
        # when we call .send or next() on the greet generator object
        # it executes
        # a. name = yield => Here it receives the value that was passed
        # to it through .send()
        # b. next statement where it immediately yields a value is also
        # executed and it pauses here
        yield f'Hi {name}! Welcome to my world'
        
def friend_name():
    g = greet()
    g.send(None)
    greeting = None
    while True:
        # f_gen.send(None) reaches till the following line and pauses
        # execution at this line, it does not execute yield
        name_from_caller = yield greeting
        greeting = g.send(name_from_caller)
        next(g)
        
friends = ['Ram', 'Hanuman', 'Laxman', 'Shatrughan', 'Bharat', 'Sita']

f_gen = friend_name()
f_gen.send(None)


for friend in friends:
    print(f_gen.send(friend))

# Concept													Is This True?		 Notes

# Does yield execute like a normal statement?				❌					It pauses, it doesn’t “run through”
# Does yield value return value to caller immediately?		✅					From the caller’s perspective, yes
# Does the coroutine continue after yield?					❌					Only on next send/next()

# Step by Step description

# 1. When we call f_gen.send(None):
#		def friend_name():
#		    g = greet()
# 			g.send(None)
#			greeting = None
#			while True:
# 				name_from_caller = yield greeting
# 				greeting = g.send(name_from_caller)
# 				next(g)

# The line in friend_name method
# 				name_from_caller = yield greeting
# is reached, yield greeting is not executed in the conventional sense that
# execution pauses here, however greeting (which is None) is returned
#
# 			def greet():
#     			while True:
#         		name = yield
#         		yield f'Hi {name}! Welcome to my world'
# In the greet function, we reach the line
# 				name = yield
# and execution pauses there, since yield does not have any value, it returns
# None to the caller - friend_name function
# friend_name function returns greeting = None back to the caller

# 2. When we call f_gen.send('Ram'):
#		def friend_name():
#		    g = greet()
# 			g.send(None)
#			greeting = None
#			while True:
# 				name_from_caller = yield greeting
# 				greeting = g.send(name_from_caller)
# 				next(g)

# The line in friend_name method
# 				name_from_caller = yield greeting
# is executed. This is where the execution had paused previously in a call to f_gen.send(None),
# The following lines are also executed
# 				greeting = g.send(name_from_caller)
# 				next(g)
# Following line in friend_name method is reached
#				name_from_caller = yield greeting
# yield greeting is not executed in the conventional sense that
# execution pauses here, however greeting (which was assigned value returned from greet method)
# is returned. At this time greeting = "Hi Ram! Welcome to my world", this is the value which was
# returned from greet method.
# greeting = "Hi Ram! Welcome to my world"
# is returned to the caller
#			print(f_gen.send('Ram'))
# f_gen.send('Ram') is the caller and it gets this value back and prints it.
#
#
# 			def greet():
#     			while True:
#         		name = yield
#         		yield f'Hi {name}! Welcome to my world'
# In the greet function, we execute the line
# 				name = yield
# This is the line where execution had previously paused. name is assigned value "Ram". Next line
#				yield f'Hi {name}! Welcome to my world'
# is not executed in the traditional sense since execution pauses here. However, because yield has
# a value "Hey Ram! Welcome to my world", this value is returned to the caller

# We can extend the above Logic to all other values in friends list