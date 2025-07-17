# import asyncio
# from time import time

# async def main():
#     print('I am in main function')
    
# print(main())
# asyncio.run(main())

# async def fetch_data():
# 	print('I am fetching data')
# 	await asyncio.sleep(1)
# 	data = { 'id': 1, 'value': 'Sam' }
# 	return data

# async def func():
#     print('Start of coroutine')
#     # Create a coroutine object
#     f = fetch_data()
#     print('End of coroutine')
#     # we await the coroutine object, we do not invoke the object
#     res = await f
#     print(f'Response :: {res}')
    
# asyncio.run(func())

# async def fetch_data(id, value):
#     print('I am fetching data')
#     await asyncio.sleep(1)
#     data = { 'id': id, 'value': value }
#     return data

# async def func():
#     task1 = asyncio.create_task(fetch_data(1, 'Ram'))
#     task2 = asyncio.create_task(fetch_data(2, 'Laxman'))
#     task3 = asyncio.create_task(fetch_data(3, 'Sita'))
    
#     res1 = await task1
#     print(f'Executed task 1 in sequence :: {res1}')
#     res2 = await task2
#     print(f'Executed task 2 in sequence :: {res2}')
    
#     res3 = await task3
#     print(f'Executed task3 in sequence :: {res3}')
    
#     print('Creating tasks and awaiting them allows us complete control over their sequencing')
    
# asyncio.run(func())

async def fetch_data(id, value, delay):
    print('I am fetching data')
    await asyncio.sleep(delay)
    data = { 'id': id, 'value': value }
    return data

# async def func():
#     start = time()
#     coroutine1 = fetch_data(1, 'Ram', 3)
#     res = await coroutine1
#     end = time()
#     print(f'Result of running coroutine 1 :: {res} - {end - start}')
    
#     start = time()
#     coroutine1 = fetch_data(2, 'Sita', 5)
#     res = await coroutine1
#     end = time()
#     print(f'Result of running coroutine 2 :: {res} - {end - start}')
    
#     start = time()
#     coroutine1 = fetch_data(3, 'Laxman', 8)
#     res = await coroutine1
#     end = time()
#     print(f'Result of running coroutine 3 :: {res} - {end - start}')

# async def func():
#     start = time()
#     task1 = asyncio.create_task(fetch_data(1, 'Ram', 3))
#     task2 = asyncio.create_task(fetch_data(2, 'Sita', 5))
#     res1 = await task1
#     res2 = await task2
#     end = time()
#     print(f'Result of running coroutines 1 & 2 :: {res1}, {res2} - {end - start}')
    
#     start = time() 
#     task3 = asyncio.create_task(fetch_data(3, 'Laxman', 8))
#     res3 = await task3
#     end = time()
#     print(f'Result of running coroutine 3 :: {res3} - {end - start}')

# async def func():
# 	start = time()
# 	task1 = asyncio.create_task(fetch_data(1, 'Ram', 3))
# 	task2 = asyncio.create_task(fetch_data(2, 'Sita', 5))
# 	results = await asyncio.gather(task1, task2)
# 	end = time()
# 	for res in results:
# 		print(f'Result of running coroutines 1 & 2 :: {res}')
    
# 	print(f'Time :: {end - start}')
    
# 	start = time() 
# 	task3 = asyncio.create_task(fetch_data(3, 'Laxman', 8))
# 	results = await asyncio.gather(task3)
# 	end = time()
# 	for res in results:
# 		print(f'Result of running coroutines 1 & 2 :: {res}')
    
# 	print(f'Time :: {end - start}')

# asyncio.run(func())


# async def func():
    # start = time()

    # task1 = asyncio.create_task(fetch_data(1, 'Ram', 20))
    # task2 = asyncio.create_task(fetch_data(2, 'Sita', 30))
    
    # results = await asyncio.gather(task1, task2)
    # for res in results:
    #     print(f'Task completed :: {res}')
    # print(f'Time taken to complete tasks :: {time() - start}')
    
    # start = time()
    # task3 = asyncio.create_task(fetch_data(3, 'Laxman', 50))
    # results = await asyncio.gather(task3)
    # for res in results:
    #     print(f'Task completed :: {res}')
    # print(f'Time taken to complete tasks :: {time() - start}')
        
# async def func():
#     tasks = []
#     start = time()
#     async with asyncio.TaskGroup() as tg:
#         for index, [name, delay] in enumerate([['Ram', 3], ['Sita', 5]]):
#             task = tg.create_task(fetch_data(index, name, delay))
#             tasks.append(task)
#     end = time()
#     results = [task.result() for task in tasks]
#     print(f'Results :: {results} -- {end - start}')
    
#     tasks = []
#     start = time()
#     async with asyncio.TaskGroup() as tg:
#         task = tg.create_task(fetch_data(3, 'Laxman', 8))
#         tasks.append(task)
#     end = time()
#     results = [task.result() for task in tasks]
#     print(f'Results :: {results} -- {end - start}')
    
# asyncio.run(func())

# async def set_future_event(future, value):
#     print('I am in set future method')
#     await asyncio.sleep(1)
#     future.set_result(value)
#     print('I am in the method')

# async def func():
#     loop = asyncio.get_running_loop()
#     future = loop.create_future()
#     asyncio.create_task(set_future_event(future, 'Future value being set'))
#     res = await future
#     print(f'Result :: {res}')
    
# asyncio.run(func())

# lock = asyncio.Lock()
# shared_resource = 0

# async def shared_access():
#     global shared_resource
#     with lock:
#         print('I am accessing shared resource')
#         shared_resource += 1
#         print(f'New value of shared resource :: {shared_resource}')
        
# async def func():
#     tasks = []
#     for _ in range(10):
#         with asyncio.TaskGroup() as tg:
#             task = tg.create_task(shared_access())
#             tasks.append(task)
        
# import asyncio

# lock = asyncio.Lock()
# shared_resource = 0

# async def shared_access():
#   global shared_resource
#   async with lock:
#     shared_resource += 1
#     await asyncio.sleep(1)
#     print(f'Shared Resource :: {shared_resource}')
    
# async def func():
#   tasks = []
#   async with asyncio.TaskGroup() as tg:
#     for _ in range(20):
#       task = tg.create_task(shared_access())
#       tasks.append(task)

#   # for task in tasks:
#   #   print(f'Result :: {task.result}')
  
# asyncio.run(func())

# import asyncio

# semaphore = asyncio.Semaphore(2)
# shared_resource = 0

# async def shared_access():
#   global shared_resource
#   async with semaphore:
#     print(f'Shared Resource :: {shared_resource}')
#     shared_resource += 1
#     await asyncio.sleep(2)
    
# async def func():
#   tasks = []
#   async with asyncio.TaskGroup() as tg:
#     for _ in range(20):
#       task = tg.create_task(shared_access())
#       tasks.append(task)
      
  # for task in tasks:
  #   print(f'Result :: {task.result}')
  
# asyncio.run(func())
  
import asyncio


async def event_signal(event):
  print('I am in the function')
  await asyncio.sleep(2)
  event.set()
  print('Event signal happened')

async def func():
  event = asyncio.Event()
  asyncio.create_task(event_signal(event))
  await event.wait()
  print('Func ended')
  

asyncio.run(func())