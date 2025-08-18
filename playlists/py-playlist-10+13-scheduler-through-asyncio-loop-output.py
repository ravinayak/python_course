from time import time
import math
import asyncio

async def search(iterable, primitive, method_name):
    for item in iterable:
        if primitive(item):
            print(f'Item Found :: {item} for Method :: {method_name}')
            return item
        await asyncio.sleep(0)

def lucas():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a + b

async def print_repititive_message(message, interval_seconds):
    count = 0
    while count < 10:
        count += 1
        print(f'**************************** {message} ****************************')
        start = time()
        expiry = start + interval_seconds
        while True:
            await asyncio.sleep(0)
            if time() >= expiry:
                break
    return 'Repititive Message function ended'

def all_primes_till_x(x):
    if x < 2:
        return
    
    if x == 2:
        return 2
    
    for num in range(3, x + 1, 2):
        is_prime = True
        for k in range(3, int(math.sqrt(num) + 1)):
            if num % k == 0:
                is_prime = False
            if is_prime:
                yield num
    
async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(search(lucas(), lambda x: len(str(x)) > 8, 'lucas'))
        task2 = tg.create_task(print_repititive_message('This is a message', 0.00015))
        task3 = tg.create_task(search(all_primes_till_x(310348), lambda x: len(str(x)) > 3, 'all_primes_till_x'))
    
    print(f'\n\n***** Printing Task Output Below *****\n')
    for task in [task1, task2, task3]:
        print(f'Task Result :: {task.result()}')
        
if __name__ == '__main__':
    asyncio.run(main())