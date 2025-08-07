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