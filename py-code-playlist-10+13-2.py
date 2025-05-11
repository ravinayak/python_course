from multiprocessing import Process, Queue
import time

# For Processes, use
# from multiprocessing import Queue
# queue = Queue()
# queue.put(name)
# queue.get()
# NO queue.task_done()
# NO queue.join()
# To block the main program thread, we must use process.join()

def ask_user(ask_user_queue):
    start = time.time()
    name = ask_user_queue.get()
    greeting = f'Hello, {name}, how are you doing today?'
    ask_user_queue.put(greeting)
    print(f'Time spent in ask_user :: {time.time() - start}')
    
def complex_calculation():
    start = time.time()
    print('Performing Scientific Computation')
    [x * x for x in range(20000000)]
    print(f'Time spent in Complex Calculation :: {time.time() - start}')
    
if __name__ == '__main__':
    start = time.time() # This will cause the program to include additional time spent
    # by user in inputting the name
    name = input('Enter your name :: ')
	# start = time.time()
	# If we put start above, it will skip the time taken by user to enter their name, and will be more
	# accurate in terms of total time obtained through addition of ask_user and complex_calculation
    ask_user_queue = Queue()
    ask_user_queue.put(name)
	
    p1 = Process(target = ask_user, args = (ask_user_queue, ))
    p2 = Process(target = complex_calculation)

    p1.start()
    p2.start()
 
    p1.join()
    p2.join()
 
    greeting = ask_user_queue.get()
    print(f'Greeting :: {greeting}')
    print(f'Time spent in Main Program :: {time.time() - start}')