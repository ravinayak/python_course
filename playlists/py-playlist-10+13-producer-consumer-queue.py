import asyncio
from collections import deque

async def friends_producer(queue: asyncio.Queue):
    friends = deque(['Ram', 'Sita', 'Laxman'])
    while friends:
        friend = friends.popleft().upper()
        print(f'Friends producer :: Putting friend into queue :: {friend}')
        await queue.put(friend)
    print('Friends producer ending ...')
    await queue.put(None)
        
async def greetings_producer(friend_queue: asyncio.Queue, greet_queue: asyncio.Queue):
    greetings = {
		'RAM': 'Hi',
		'SITA': 'Hello',
		'LAXMAN': 'Welcome'
	}
    while True:
        friend = await friend_queue.get()
        if friend is None:
            print(f'Greetings producer received sentinel, ending...')
            await greet_queue.put(None)
            break
        friend_queue.task_done()
        
        greet_msg = f'{greetings[friend]} {friend}'
        print(f'Greetings producer :: Putting greetings into queue :: {greet_msg}')
        await greet_queue.put(greet_msg)
        
async def consumer(greet_queue: asyncio.Queue, results_queue: asyncio.Queue):
    while True:
        greeting = await greet_queue.get()
        if greeting is None:
            await results_queue.put(None)
            print('Consumer Received sentinel ending ...')
            break
        print(f'Consumer receieved greeting :: {greeting}')
        await results_queue.put(greeting)
        
async def main():
    friend_queue = asyncio.Queue()
    greet_queue = asyncio.Queue()
    # This queue is to get the results back from the consumer
    # We cannot return from the consumer, else it will break
    # the data pipeline meaning consumer will stop execution
    results_queue = asyncio.Queue()
    await asyncio.gather(
		asyncio.create_task(friends_producer(friend_queue)),
		asyncio.create_task(greetings_producer(friend_queue, greet_queue)),
		asyncio.create_task(consumer(greet_queue, results_queue))
	)
    while True:
        result = await results_queue.get()
        if result is None:
            print('Main program exiting ...')
            break
        print(f'Result from the consumer :: {result}')
        results_queue.task_done()
               
asyncio.run(main())
        
