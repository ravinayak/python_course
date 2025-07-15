# from types import coroutine
# from collections import deque
# import asyncio

# friends = deque(['Ram', 'Sita', 'Gaurav'])

# @coroutine
# async def friend_upper():
# 	while friends:
# 		friend = friends.popleft().upper()
# 		greeting = f'Hi {friend}! Welcome to the club'
# 		print(greeting)
  
# async def greet():
#     f = friend_upper()
#     res = await f
#     return res

# asyncio.run(greet())


# Example below demonstrates how we can use coroutine and async methods to
# send values to a generator and receive values back.
# Normally we cannot use async method with a generator, as in we cannot
# await a generator but because we have labeled it as a coroutine, it works
#
from types import coroutine
from collections import deque

friends = deque(('Ram', 'Sita', 'Laxman'))

@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = f'Hey {friend} How you doing?'
        yield greeting
        
async def greet():
    f = friend_upper()
    res = await f
    return res

g = greet()

print(g.send(None))

for x in range(len(friends)):
	try:
		print(g.send(x))
	except StopIteration:
		print('End Reached')

