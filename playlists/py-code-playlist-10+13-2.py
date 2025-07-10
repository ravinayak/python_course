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
    
# This class is an example of a generator which can be used to run
# tasks instead of threads
# Instead of initializing list with an array of elements, we shall
# initialize list with an array of methods to be executed
# This list will be looked up by an index, and the method at that index
# will be returned while the index of the perform_task object will be
# incremented to return method at next index when next(...) is called on
# the task_object
# When we reach the end of the list in task_object, a StopIteration exception
# will be raised signaling the end of methods in the current perform_task
# object to be performed
class PerformTask:
	def __init__(self, task_num, routines):
		self.routines = routines
		self.task_num = task_num
		self.index = 0
	
	def __next__(self):
		if self.index < len(self.routines):
			current = self.index
			self.index += 1
			return self.routines[current]
		else:
			raise StopIteration('No More Elements to return')

task1 = PerformTask(1, list(range(10)))
task2 = PerformTask(2, list(range(20)))
task3 = PerformTask(3, list(range(5)))

# All Perform_task objects are included in a master tasks list
# and are executed one after the other in sequence until each
# perform_task object is exhausted
# A perform_task object is removed from the list, executed
# and then again appended back to the list(if it still contains
# more tasks to perform)
# The sequence of execution of task_objects to be executed is:
#       tasks initial sequence => [1, 3, 2]
#   [1, 3, 2, 1, 3, 2, 1, 3, 2....]: Same Sequence will repeat
# until a task is exhausted of all the methods

tasks = [task1, task3, task2]

while tasks:
	try:
		task = tasks[0]
		tasks.remove(task)
		task_num = task.task_num
		x = next(task)
		print(f'Task{task_num} :: {x}')
		tasks.append(task)
	except StopIteration as exc:
		print(f'Task{task_num} finished')
