from threading import Thread
from queue import Queue
import time
import random

counter = 0
counter_queue = Queue()
job_queue = Queue()

def increment_manager():
    global counter
    while True:
        increment = counter_queue.get()
        time.sleep(random.random())
        old_counter = counter
        counter = old_counter + increment
        time.sleep(random.random())
        job_queue.put((f'New Counter Value : {counter}', '----------'))
        counter_queue.task_done()

        
def print_manager():
    while True:
        for line in job_queue.get():
            time.sleep(random.random())
            print(line)
            time.sleep(random.random())
        job_queue.task_done()
        
counter_thread = Thread(target = increment_manager, daemon = True)
print_thread = Thread(target = print_manager, daemon = True)

counter_thread.start()
print_thread.start()

def increment_counter():
    print('Thread Putting Value in Counter Queue......')
    time.sleep(random.random())
    counter_queue.put(1)
    time.sleep(random.random())


worker_threads = [Thread(target = increment_counter) for _ in range(10)]

def start_join_threads(thread_lists):
	for thread_list in thread_lists:
		for thread in thread_list:
			thread.start()
			time.sleep(random.random())
   
	for thread_list in thread_lists:
		for thread in thread_list:
			thread.join()
			time.sleep(random.random())

start_join_threads([worker_threads])

counter_queue.join()
job_queue.join()
    