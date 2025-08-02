from types import coroutine

day_activities_dict = {
    None: None,
	'Sun': 'Wake up and Study',
	'Mon': 'Go to Office',
	'Tue': 'Work from home and study',
	'Wed': 'Go to office and finish PR'
}

@coroutine
def greet():
	name = None
	while True:
		name = yield(day_activities_dict[name])
		greeting = f'Today is {name}! Welcome to a new day.'
		print(greeting)
  
async def weekday_name(g):
	await g

w_gen = weekday_name(greet())

# None is returned at this point, so we are not printing it
# print(f'Value returned :: {w_gen.send(None)}')
w_gen.send(None)

weekdays = ['Sun', 'Mon', 'Tue', 'Wed']

print(f'**********************************\n')
for day in weekdays:
	activity = w_gen.send(day)
	print(f'Activity :: {activity}')
	print()
print(f'**********************************\n')

import asyncio
from types import coroutine

# @coroutine
# async def gen_fib():
#     a = 1
#     b = 1
#     fib = 1
#     while True:
#         yield fib
#         fib = a + b
#         a, b = b, fib
        
# async def main():
#     fib = gen_fib()
#     for _ in range(10):
#         res = await fib.asend(None)
#         print(f'Res :: {res}')
        
# asyncio.run(main())

@coroutine
async def gen_fib(x):
    a = 1
    b = 1
    fib = { None: None, 1: 1, 2: 1 }
    for x in range(3, 1000):
        fib[x] = a + b
        a, b = b, fib[x]
    
    res = None
    while True:
        res = yield fib[res]
        
async def main():
    z = [ 1, 3, 5, 8, 10, 11, 12, 13, 25, 35, 65, 100, 110, 200, 250]
    fib = gen_fib(None)
    await fib.asend(None)
    for x in z:
        res = await fib.asend(x)
        print(f'{x}th Fibonnaci number :: {res}')
        
asyncio.run(main())