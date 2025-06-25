from threading import Thread, Lock
from queue import Queue
import time
import random

# For threading, use
# from queue import Queue
# Alternative to above import is to use:
#   a. import queue
#   b. queue = queue.Queue()
# queue = Queue()
# queque.put(name)
# queue.get()
# queue.task_done()
# queue.join()
# 🔁 queue.join() (from queue.Queue)

# Purpose:
# 	•	Blocks the calling thread until all tasks in the queue have been processed.

# How it works:
# 	•	Each q.put(item) adds an item and increments an internal counter.
# 	•	Each q.task_done() decrements that counter.
# 	•	q.join() blocks until the counter is zero (i.e., every put() has a corresponding task_done()).

counter = 0
counter_queue = Queue()
job_queue = Queue()

def counter_manager():
    time.sleep(random.random())
    with Lock():
        count = counter_queue.get()
        time.sleep(random.random())
        # print(f'Counter Manager - Counter Value :: {count}')
        time.sleep(random.random())
        job_queue.put((f'Job Queue Manager - Counter Value :: {count}', '----'))
        counter_queue.task_done()
    
def job_manager():
    while True:
        for line in job_queue.get():
            time.sleep(random.random())
            print(line)
        job_queue.task_done()
        time.sleep(random.random())
            
def increment_manager():
    for x in range(10):
        counter_queue.put(x)

increment_manager()
Thread(target = job_manager, daemon = True).start()

thread_list = []
for _ in range(10):
    thread_list.append(Thread(target = counter_manager))
    
for t in thread_list:
    t.start()
    
counter_queue.join()
job_queue.join()

