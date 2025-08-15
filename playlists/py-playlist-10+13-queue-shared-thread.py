from queue import Queue
from threading import Thread
from time import sleep
from random import random

counter = 0
counter_queue = Queue()
printer_queue = Queue()
STOP_SIGNAL = 'STOP'

def increment_counter():
	global counter
	while True:
		try:
			increment = counter_queue.get(timeout=1)
			sleep(random())
			print(f'Value retrieved from Counter Queue :: {increment} - Old counter :: {counter}')
			counter = counter + increment
			sleep(random())
			printer_queue.put(counter)
			counter_queue.task_done()
		except:
			continue

def printer_manager():
    while True:
        try:
            line = printer_queue.get(timeout=1)
            if line == STOP_SIGNAL:
                printer_queue.task_done()
                break
            else:
                print(f'Value retrieved from Printer Queue :: {line}')
                printer_queue.task_done()
        except:
            continue
        
def counter_queue_put():
    counter_queue.put(1)

def main():
    workers = [Thread(target=counter_queue_put) for _ in range(10)]
    for w in workers:
        w.start()
        
    for w in workers:
        w.join()
        
    Thread(target=increment_counter, daemon=True).start()
    Thread(target=printer_manager, daemon=True).start()
    
    counter_queue.join()
    
    printer_queue.put(STOP_SIGNAL)
    printer_queue.join()
                
if __name__ == '__main__':
    main()