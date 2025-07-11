
def friends_upper():
    friends = ['Rolf', 'Hose', 'Rahul', 'Sam', 'Kim']
    for friend in friends:
        try:
            greeting = yield
            print(f'{greeting}, How are you doing today? {friend}')
        except StopIteration:
            pass

def greet(friend_upper):
    friend_upper.send(None)
    while True:
        greet = yield
        friend_upper.send(greet)

friend_upper = friends_upper()
g = greet(friend_upper)
g.send(None)

# send is used to send values to a generator, it differs from next in 2 ways:
# 1. next does not pass any value to the generator, simply calls the next yield
# 2. send raises StopIterationError only the last call to send where as next
#	 does not raise StopIterationError on the last call, it raises error on the 
#	 (last + 1)th call
#
# def gen():
#     for i in range(5):
#         val = yield i
#         print(f"Received: {val}")
        
# g = gen()
# next(g)        # Start the generator
# g.send("one")  # Works
# g.send("two")  # Works
# g.send("three")
# g.send("four")
# g.send("five")  # ❌ Raises StopIteration

# Why does send("five") raise StopIteration?

# Because after processing the final value, the generator function completes — there are
# no more yields left. When you do send("five"), Python:
# 	1.	Sends "five" into the last paused yield
# 	2.	Runs the code after it (print(...))
# 	3.	Finds that the generator is done (loop ends)
# 	4.	Python implicitly raises StopIteration

# So the last send() is the one that raises — not the next one.

# But next() behaves differently:

# If you had just used:

# g = gen()
# print(next(g))  # 0
# print(next(g))  # 1
# print(next(g))  # 2
# print(next(g))  # 3
# print(next(g))  # 4
# print(next(g))  # ❌ Raises StopIteration

# The StopIteration is raised after the last yielded value — cleanly and as expected.
# There’s no value being injected, so no confusion.

# | Generator Status     | `next()` Behavior                                   | `send(value)` Behavior                                                    |
# |----------------------|-----------------------------------------------------|---------------------------------------------------------------------------|
# | Mid-execution        | Advances to the next `yield`, returns yielded value | Sends `value` into current `yield`, resumes execution to next `yield`     |
# | At final `yield`     | Returns final value, then raises `StopIteration`    | Sends `value` into final `yield`, resumes execution, then raises `StopIteration` |
# 						   on next call
# | After completion     | Raises `StopIteration` immediately                  | Raises `StopIteration` immediately (may cause `RuntimeError` if uncaught) |


greetings = ['Hi', 'Hello', 'Hola', 'Jola']
for greet in greetings:
    print(greet)
    g.send(greet)
    
    
def greet():
    while True:
        # Here we receive the data
        name = yield()
        message = f'Hi! {name}'
        print(f'greet Generator yielding message :: {message}')
        print('************************************************************')
        
def friend_name():
    # Create a generator object
	g = greet()
	# TypeError: can't send non-None value to a just-started generator
	# This error occurs because a generator function needs to be "primed" before
 	# you can send data into it.

	# When you create a generator object (e.g., g = greet()), the code inside the
 	# function has not yet run.
	# To start it, you must call next(g) or g.send(None). This runs the code up to the
 	# very first yield expression and then pauses the generator there.
	# Only after it's paused at a yield can it accept a value from a subsequent .send() call.
	
	# Prime the generator here by calling g.send(None). This executes greet() generator 'g'
	# upto the very 1st yield and pauses it there, so that every subsequent g.send(x) calls
	# will reach the yield and the value will be accepte
	g.send(None)
	while True:
		# This is where it receives data when the method is called
		# with a parameter
		# yield can return a value when called with 'next', it can
		# also consume a value when called without any parameter,
		# this is an example of when it is called without any parameter
		# and it consumes data sent to the generator object through
		# 'send' called on the object
  
		# f_gen.send(None) primes this generator and reaches this line
		# of code and pauses at the yield. When we send a value to this
		# generator, it is yielded and g.send(name) sends this value to
		# to the greet() generator 'g', which has already been primed at
		# line number 24. yield of 'g' is paused at yield and can accept
		# any values sent to it
		name = yield()
		print('************************************************************')
		print(f'friend_name generator - Received Name :: {name}')
		g.send(name)

friends = ['Rat', 'Jat', 'Sat', 'Mon']

f_gen = friend_name()

# This is where we prime the generator
f_gen.send(None)

for friend in friends:
	f_gen.send(friend)