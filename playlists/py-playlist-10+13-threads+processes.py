from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
from threading import Thread
from multiprocessing import Process
from time import time
from timeit import timeit

def ask_user():
    start = time()
    user_name = input('Enter your name :: ')
    print(f'Hi {user_name}! Welcome to the show')
    print(f'ask_user function completed, Time taken for ask_user function :: {time() - start }')
    
def scientific_calculation():
    start = time()
    [x**2 for x in range(5000000)]
    print(f'Scientific Calculation completed, Total time taken :: {time() - start}')
    
def main():
    start = time()
    ask_user()
    scientific_calculation()
    print(f'Time taken to run both functions in code :: {time() - start }')
    
    start = time()
    t = Thread(target = ask_user)
    t.start()
    scientific_calculation()
    t.join()
    print(f'Time taken to complete both functions when ask_user is running in a thread :: {time() - start }')
    
    start = time()
    p1 = Process(target = scientific_calculation)
    p2 = Process(target = scientific_calculation)
    p1.start()
    p2.start()
    print('Both Processes started')
    p1.join()
    p2.join()
    print(f'Total time taken to finish scientific calculation running as processes :: {time() - start}')
    
def main_exec():
    start = time()
    with ThreadPoolExecutor(max_workers = 2) as pool:
        pool.submit(ask_user)
        pool.submit(scientific_calculation)
    print(f'Time taken to run using pool for ask_user :: {time() - start}')    
    
    with ProcessPoolExecutor(max_workers = 2) as pool:
        pool.submit(scientific_calculation)
        pool.submit(scientific_calculation)
    print(f'Time taken to run processes using pool :: {time() - start}')
    
    print(f'Time taken using timeit module :: {timeit('[x**2 for x in range(100)]')}')
    
if __name__ == '__main__':
    main()
    main_exec()

    