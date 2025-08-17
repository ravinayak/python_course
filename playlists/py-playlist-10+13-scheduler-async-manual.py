import math
from time import time
from collections import deque

def async_lucas():
    a = 2
    b = 1
    yield 2
    while True:
        yield b
        a, b = b, a + b

def async_search(iterable, predicate):
    for item in iterable:
        print(f'I am in async search with item :: {item}')
        if predicate(item):
            return item
        yield
    raise ValueError('not found')

def async_all_primes(x):
    if x < 2:
        return
    
    if x == 2:
        yield 2
        
    for j in range(3, x + 1, 2):
        is_prime = True
        for k in range(3, int(math.sqrt(j)) + 1):
            if j % k == 0:
                is_prime = False
                break
        if is_prime:
            yield j
    
def async_print_repititive_message(message, interval_time):
    count = 0
    while count < 1110:
        count += 1
        print(f'****************************************** {message} ******************************************')
        start = time()
        expiry = start + interval_time
        while True:
            print('About to yield')
            yield
            now = time()
            if(now >= expiry):
                break

class Task:
    next_id = 0

    def __init__(self, routine):
        self.routine = routine
        self.id = Task.next_id
        Task.next_id = Task.next_id + 1
        
    def __repr__(self):
        return(f'Task id {self.id} -- routine :: {self.routine}')
        
class Scheduler:
    def __init__(self):
        self.runnable_tasks = deque()
        self.completed_tasks = {}
        self.failed_tasks = {}
        
    def add(self, task):
        self.runnable_tasks.append(task)
        
    def run_to_completion(self):
        while len(self.runnable_tasks) != 0:
            task = self.runnable_tasks.popleft()
            print('Running Task with id {}'.format(task.id))
            try:
                yielded = next(task.routine)
                print(f'Task {task.id} yielded: {yielded}')
            except StopIteration as stopped:
                print(f'Task with id {task.id} finished execution and yielded value :: {stopped.value}')
                self.completed_tasks[task.id] = stopped.value
            except Exception as ex:
                print(f'Task with id {task.id} failed execution :: {ex}')
                self.failed_tasks[task.id] = ex
            else:
                print(f'Task {task.id} is being appended back to queue')
                self.runnable_tasks.append(task)
                
def main():
    task1 = Task(async_search(async_lucas(), lambda x: len(str(x)) >= 10))
    task2 = Task(async_print_repititive_message('This is a message being printed', 0.00015))
    task3 = Task(async_search(async_all_primes(150000), lambda x: len(str(x)) >= 6))
    sc = Scheduler()
    sc.add(task1)
    sc.add(task2)
    sc.add(task3)
    sc.run_to_completion()
    
if __name__ == '__main__':
    main()