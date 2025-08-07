import asyncio

class CustomAwait:
	def __init__(self, n):
		self.n = n
  
	def __await__(self):
		print('Custom Await Class object await method being called')
		yield
		print('Await method exiting')
        
async def main():
    ca = CustomAwait(20)
    await ca
    
asyncio.run(main())

import asyncio
from unsync import unsync
import time
import math

@unsync
def sync_task(name):
  print(f'Task started :: {name}')
  print('Sleeping for 2 seconds - synchronous blocking - shall be executed using ThreadPoolExecutor')
  time.sleep(2)
  print('Exiting the synchronous method')
  return f'Syncronous Task :: {name}'
  
@unsync
async def async_task(name):
  print(f'Task started :: {name}')
  print('Asynchronous sleep for 2 seconds - asyncronous non blocking - shall be executed in an async event loop')
  await asyncio.sleep(2)
  print('Exiting the async method')
  return f'Asynchronous Task :: {name}'
  
@unsync(process = True)
def cpu_task(name, x):
  print(f'Task started :: {name}')
  print('Task performing cpu bound activity')
  print(f'Sqrt(x) :: {math.sqrt(x)}')
  print('Task exiting')
  return f'CPU Task :: {name}'
  
def callback_fn(fut):
  print(f'This is a demo callback which will be called when the future completes with the result :: {fut.result()}')

async def main():
  futures = [
		sync_task('Thread'),
		async_task('Asyncio-Event-Loop'),
		cpu_task('Cpu-Bound-Process', 200000)
	]
  for f in futures:
    print(f'Callback shall be called when future completes :: {f.future.add_done_callback(callback_fn)}')
    print(f'Type of future object :: {type(f)}')
    
  for f in futures:
    result = f.result()
    print(f'Result of Task :: {result}')
    print(f'Task done :: {f.done()}')
    print(f'Exception :: {f.future.exception()}')
    
asyncio.run(main())

import asyncio
import time

async def co1():
    print('Co-routine1 started')
    [x ** 2 for x in range(2000000)]
    print('Co-routine1 going to sleep for 1 seconds')
    await asyncio.sleep(1)
    print('Co-routine1 resumed after sleep and going to perform operation')
    start = time.time()
    [x ** 2 for x in range(200000000)]
    print(f'Time taken :: {(time.time() - start):.3f} seconds')
    print('Co-routine1 performed operation and now exiting')
    return 1

async def co2():
    print('Co-routine2 started')
    [x ** 2 for x in range(2000000)]
    print('Co-routine2 going to sleep for 5 seconds')
    start = time.time()
    await asyncio.sleep(5)
    print(f'Co-routine2 resumed after sleep and now exiting, time taken :: {(time.time() - start):.3f} seconds')
    return 5
    
async def main():
    # asyncio.gather runs tasks concurrently by starting the tasks all at once
    results = await asyncio.gather(co1(), co2())
    for res in results:
        print(f'Res :: {res}')
    
asyncio.run(main())

import asyncio
import time

class CustomAwaitable:
    def __init__(self, limit):
        self.limit = limit
        
    def __await__(self):
        # We cannot use await inside __await__ method since it is not a coroutine
        # there are ways around it though
        yield
        time.sleep(3)
        print('Custom Awaitable await method finished')

async def main():
    ca = CustomAwaitable(10)
    await ca
    
asyncio.run(main())