# Python Secrets and Advanced Concepts

A collection of useful Python tips and explanations for more advanced concepts.

---

## `__str__` vs. `__repr__`: How `print()` Behaves

A common point of confusion is how Python decides to represent an object as a string. The key is to understand the difference between `__str__` and `__repr__` and how `print()` uses them.

- `print(object)` will try to use the `__str__()` method of the object. This is meant to be a user-friendly, readable representation.
- If `__str__()` is not defined, it falls back to `__repr__()`.
- When you print a container like a list (`print([object])`), the list's `__repr__` method is called, which in turn calls the `__repr__()` method of each object inside it. `__repr__()` is meant to be an unambiguous, developer-friendly representation that could ideally be used to recreate the object.

### Example

```python
class MyObject:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"A user-friendly string: {self.value}"

    def __repr__(self):
        return f"MyObject(value={self.value!r})"

obj = MyObject(10)

# print(object) uses __str__
print(obj)

# print([object]) uses __repr__ for the object inside the list
print([obj])
```

**Output:**

```
A user-friendly string: 10
[MyObject(value=10)]
```

---

## Generators and Coroutines

### Understanding the `TypeError: can't send non-None value to a just-started generator`

This error is a classic "rite of passage" when working with generator-based coroutines.

**The Problem:** A generator function's code does not run until you "prime" it. You cannot send a value (`.send(value)`) to a generator that hasn't started executing and paused at its first `yield` expression.

**The Solution:** You must first call `next(g)` or `g.send(None)` to advance the generator to its first `yield` point. Only then can it accept a non-`None` value.

### Example

```python
def my_coroutine():
    print("-> Coroutine started")
    value = yield
    print(f"-> Coroutine received: {value}")
    yield

co = my_coroutine()

# This will cause the TypeError:
# co.send("Hello")

# Correct way: Prime the coroutine first
print("Priming the coroutine...")
next(co)  # or co.send(None)
print("Coroutine is primed and waiting at the first yield.")

# Now we can send a value
print("Sending value to coroutine...")
co.send("Hello")
```

**Output:**

```
Priming the coroutine...
-> Coroutine started
Coroutine is primed and waiting at the first yield.
Sending value to coroutine...
-> Coroutine received: Hello
```

### What is a Coroutine?

> 🚀 **In Simple Terms:** Think of a coroutine as a “function that can take a break.” While normal functions run from start to finish without stopping, coroutines can pause (using `yield`), let other code run, and then pick up exactly where they left off when a value is sent back to them.

> 📘 **Why Use Coroutines?** They are incredibly efficient for handling asynchronous tasks, such as:
>
> - Making API calls
> - Reading from files or network sockets
> - Waiting for user input
>
> They help you write non-blocking code that can handle many operations concurrently.

### A Classic Coroutine Example

Here is a simple coroutine that yields a value and then waits to receive a value back.

```python
def simple_coroutine():
    print("Coroutine started")
    x = yield 42  # Pauses here, returns 42, and waits for a value to be sent
    print(f"Received: {x}")

# 1. Create the coroutine object
co = simple_coroutine()

# 2. Prime the coroutine
#    - It runs up to the first yield.
#    - It prints "Coroutine started".
#    - It yields the value 42.
value_from_yield = next(co)
print(f"Value from first yield: {value_from_yield}")

# 3. Send a value back into the coroutine
#    - The coroutine resumes.
#    - The value 100 is assigned to 'x'.
#    - It prints "Received: 100".
#    - The function finishes, raising StopIteration.
try:
    co.send(100)
except StopIteration:
    print("Coroutine finished.")
```

### Key Coroutine Concepts

| Concept       | Meaning                                                                                                |
| ------------- | ------------------------------------------------------------------------------------------------------ |
| `yield`       | In a coroutine, it pauses the function, returns a value, and waits for a value to be sent back.        |
| `send(value)` | Resumes the coroutine from its last `yield` point and passes `value` into it.                          |
| `next()`      | Starts or resumes the coroutine until the next `yield`. It's equivalent to `send(None)`.               |
| `await`       | Used in modern Python (3.5+) with `async def` functions to pause execution on other awaitable objects. |

1. Can a coroutine accept and return data at the same time?
   Yes, this is the core feature of a classic generator-based coroutine! However, it's not happening in the exact same instant. It's a two-step sequence that happens at a single point in your code: the yield expression.

Returning Data: When a coroutine's execution reaches a yield statement, it yields (returns) a value to the caller and pauses its execution at that exact spot.
Accepting Data: The caller can then use the .send() method to resume the coroutine. The value passed to .send() becomes the result of the yield expression inside the coroutine, effectively passing data into it.
The simple_coroutine example from your python_secrets.md file is perfect for illustrating this:

```
def simple_coroutine():
    print("-> Coroutine started")
    # This is the key line:
    # 1. It yields the value 42 and pauses.
    # 2. When resumed, the value sent in is assigned to 'x'.
    x = yield 42
    print(f"-> Received: {x}")

# --- Execution Flow ---

# 1. Create the coroutine; no code has run yet.
co = simple_coroutine()

# 2. Prime the coroutine by calling next().
#    - It runs until the `yield 42`.
#    - It prints "-> Coroutine started".
#    - It RETURNS the value 42 and pauses.
value_from_yield = next(co)
print(f"Caller received: {value_from_yield}")

# 3. Send data back into the paused coroutine.
#    - The coroutine resumes.
#    - The value 100 is ACCEPTED and assigned to 'x'.
#    - It prints "-> Received: 100".
#    - The function ends, raising StopIteration.
try:
    co.send(100)
except StopIteration:
    print("-> Coroutine finished.")
```

Output:

```
-> Coroutine started
Caller received: 42
-> Received: 100
-> Coroutine finished.
```

So, a single x = yield 42 line both sends data out (42) and, upon resuming, receives data in (100).

2. Is a thread not better suited than a coroutine for handling user input?
   For handling a standard, blocking input() call, yes, a thread is almost always a better and more straightforward solution than a coroutine.

Here’s why:

The Threading Approach (Simpler and More Direct)
The input() function is a blocking operation. It halts the execution of its thread until the user types something and presses Enter.

By placing the input() call in a separate thread, you allow your main program to remain responsive and perform other computations while the dedicated input thread is blocked. This is a classic and highly effective use case for threading.

Your own example code in 1_threads.py demonstrates this perfectly. The complex_calculation can run at the same time the program is waiting for user input.

```
# Based on /Users/ravikumarnayak/personal_projects/python/The-Complete-Python-Course/13_async_development/sample_code/1_threads.py
from threading import Thread
import time

def ask_user():
	user_input = input('Enter your name: ')
	print(f'Hello, {user_input}')

def complex_calculation():
	print('Started calculating...')
	[x**2 for x in range(20000000)]
	print('Finished calculating.')

thread1 = Thread(target=complex_calculation)
thread2 = Thread(target=ask_user)

start = time.time()
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(f'Two thread total time: {time.time() - start:.2f}s')
```

When you run this, the "Started calculating..." message appears immediately, and you can type your name while the calculation happens in the background. The total time will be that of the longest task, not the sum of both.

The Coroutine (asyncio) Approach (More Complex)
Modern coroutines with async/await run on a single-threaded event loop. If you call a blocking function like input() inside an async function, it will block the entire event loop. No other coroutines can run, and your application will freeze, defeating the entire purpose of asyncio.

The Wrong Way (Don't do this!):

```
import asyncio

async def ask_user_badly():
    # This will freeze the event loop!
    user_input = input('Enter your name: ')
    print(f'Hello, {user_input}')

async def other_task():
    print("Other task starting...")
    await asyncio.sleep(2)
    print("Other task finished.")

# If you run these together, other_task will not start its sleep
# until AFTER the user has provided input.
# await asyncio.gather(ask_user_badly(), other_task())

```

The Correct (but more complex) Way:

To properly handle a blocking call in asyncio, you must run it in a separate thread managed by an executor, which prevents it from blocking the main event loop.

```
import asyncio
import time

def blocking_ask_user():
    """A standard function with a blocking call."""
    user_input = input('Enter your name: ')
    print(f'Hello, {user_input}')

async def main():
    loop = asyncio.get_running_loop()
    start = time.time()

    # Schedule the blocking function to run in the default thread pool executor
    input_task = loop.run_in_executor(
        None, blocking_ask_user
    )

    # Create another concurrent task
    calculation_task = asyncio.sleep(3) # Simulates a 3-second async operation

    print("Calculation and user input are running concurrently.")
    await asyncio.gather(input_task, calculation_task)
    print(f"Total time: {time.time() - start:.2f}s")

asyncio.run(main())
```

As you can see, while it's possible with asyncio, it requires the extra step of using run_in_executor. For the simple case of handling input(), the threading module provides a much more direct and readable solution.

###If I ran a loop for a co routine, would it be able to accept data and return data at the same time? give me an example?

Yes, a coroutine running in a loop can absolutely accept data and return data in a continuous cycle. The key is the yield expression, which acts as a two-way communication channel.

When the caller uses .send(value), it sends data into the coroutine.
The yield expression inside the coroutine receives that value, processes it, and then yields a new value back to the caller.
This creates a "ping-pong" effect where the caller's loop and the coroutine's loop are in sync, exchanging data on each iteration.

Example: A Running Average Coroutine
Here is a practical example. We'll create a coroutine that runs in an infinite loop. On each iteration, it accepts a number, updates its internal state, and returns the new running average.

```
def running_averager():
    """
    A coroutine that maintains a running average.
    It accepts a number and yields the current average.
    """
    print("-> Coroutine started, ready to receive values.")
    # Initialize internal state
    total = 0.0
    count = 0
    average = None

    while True:
        # The magic happens here:
        # 1. The coroutine yields the `average` and PAUSES.
        # 2. When the caller .send()s a value, it RESUMES.
        # 3. The sent value is assigned to `term`.
        term = yield average

        # Process the received data and update state
        print(f"   -> Coroutine received: {term}")
        total += term
        count += 1
        average = total / count

# --- The Caller Code ---

# 1. Create the coroutine object.
averager = running_averager()

# 2. Prime the coroutine. This is essential!
#    We call next() to run the code up to the first `yield`.
#    It will yield its initial `average` (which is None) and then pause.
#    The documentation in your `python_secrets.md` file explains this perfectly.
next(averager)

# 3. Now, loop and send data to the coroutine.
#    The .send() call both sends a value and receives the next yielded value.
for number in [10, 20, 60, 30]:
    print(f"Caller: Sending {number}...")
    # Send the number in and get the calculated average back.
    current_average = averager.send(number)
    print(f"Caller: Current average is {current_average:.2f}\n")

# 4. Close the coroutine to clean up (good practice).
averager.close()
print("-> Coroutine closed.")
```

### Execution Breakdown

Let's trace the execution to see how the data flows:

averager = running_averager(): Creates the coroutine object, but no code inside it runs yet.
next(averager): Primes the coroutine.
-> Coroutine started... is printed.
The while True loop starts.
It hits term = yield average. It yields the value of average (which is None) and pauses, waiting for data.
averager.send(10):
The caller sends 10 into the paused coroutine.
10 is assigned to the term variable.
-> Coroutine received: 10 is printed.
total becomes 10, count becomes 1, average becomes 10.0.
The while loop repeats, hitting yield average again. It yields 10.0 back to the caller and pauses.
The caller receives 10.0, assigns it to current_average, and prints it.
averager.send(20):
The caller sends 20.
20 is assigned to term.
-> Coroutine received: 20 is printed.
total becomes 30, count becomes 2, average becomes 15.0.
The coroutine yields 15.0 back to the caller and pauses.
The caller receives 15.0 and prints it.
This cycle continues, with the coroutine maintaining its state (total and count) across multiple send calls, which is something a normal function cannot do.

```
-> Coroutine received: 20 is printed.
total becomes 30, count becomes 2, average becomes 15.0.
The coroutine yields 15.0 back to the caller and pauses.
The caller receives 15.0 and prints it. This cycle continues, with the coroutine maintaining its state (`total` and `count`) across multiple `send` calls, which is something a normal function cannot do.

---
```

**A function can be async and a generator at the same time**

## Asynchronous Generators (`async def` + `yield`)

Since Python 3.6, a function **can** be both `async` and a generator. This powerful feature, called an **asynchronous generator**, allows you to `await` asynchronous operations and then `yield` a result in a sequence.

This is perfect for streaming data that requires an async call for each chunk (e.g., fetching pages from a web API).

### How It Works

- It is defined with `async def`.
- It uses `yield` to produce values.
- It can use `await` to pause for other coroutines.
- It is consumed using an `async for` loop.

### Example

Here is an asynchronous generator that counts down, waiting for one second between each number it yields.

```python
import asyncio

async def async_countdown(n):
    """
    An asynchronous generator that counts down from n,
    waiting 1 second between each yield.
    """
    print("-> Countdown started!")
    while n > 0:
        await asyncio.sleep(1)  # Pauses for an async operation
        yield n                 # Yields a value
        n -= 1
    print("-> Countdown finished!")

async def main():
    # You consume an async generator with `async for`
    print("Starting the async for loop...")
    async for number in async_countdown(3):
        print(f"   Received number: {number}")
    print("Async for loop finished.")

# Run the main coroutine
asyncio.run(main())
```

**Output:**

```
Starting the async for loop...
-> Countdown started!
   Received number: 3
   Received number: 2
   Received number: 1
-> Countdown finished!
Async for loop finished.
```

### is a coroutine always defined using async?

Great question!

🧠 No, a coroutine in Python is not always defined using async def — though that is the modern and preferred way.

There are two types of coroutines in Python:

⸻

✅ 1. Modern Coroutines — using async def (Python 3.5+)

These are what most people mean when they say “coroutine” today.

```
async def say_hi():
    return "Hello"

coro = say_hi()
print(type(coro))  # <class 'coroutine'>
```

You can await these:

```
import asyncio
asyncio.run(say_hi())
```

✅ 2. Generator-based Coroutines — using @types.coroutine (Legacy Style)

Before async def, coroutines were built with yield + @coroutine.

```
from types import coroutine

@coroutine
def legacy_coro():
    yield
    return 42

c = legacy_coro()
print(type(c))  # <class 'generator'>
```

These behave like coroutines, but are actually generators with a special **await**() method under the hood.

They can be awaited too:

```
async def main():
    result = await legacy_coro()
    print(result)

import asyncio
asyncio.run(main())
```

🔍 Summary Table

```

Definition Style                    Awaitable?              Common Today?                   Underlying Type
-----------------                   -----------------       ----------------------------    -----------------------------

1. async def                        ✅ Yes                  ✅ Yes                          coroutine

2. def + yield + @coroutine         ✅ Yes                  ⚠️ Rare                         generator with __await__()

3. def + yield (no decorator)       ❌ No                   ✅ Yes (but not a coroutine)    generator


```

✅ TL;DR

    •	A coroutine is not always defined with async def
    •	But in modern Python, you should always use async def unless you’re writing low-level async libraries
    •	@coroutine is still useful for creating awaitable wrappers around generators, but it’s mostly legacy

### 🧠 What Is an Event Loop?

The event loop is a mechanism that waits for tasks (coroutines, I/O events, timers, etc.) to be ready, and then runs them one at a time in a loop — cooperatively, not in parallel.

Think of it like a scheduler that:
• Keeps track of what needs to run
• Runs whatever is ready without blocking
• Suspends tasks that are waiting (e.g., sleeping, I/O)
• Resumes tasks when their data is ready

⸻

🧱 Analogy

🕹️ Imagine a single-threaded robot that:
• Checks all its tasks in a list
• Runs each task until it hits an “await”
• Puts it aside and goes to the next ready task
• Comes back later when the paused task can continue

⸻

✅ Basic Event Loop Flow 1. You define one or more coroutines (async def) 2. You submit them to the event loop 3. The loop starts running and manages when each coroutine is allowed to run next 4. When a coroutine awaits, it’s paused 5. The event loop resumes it later when it’s ready

⸻

🧪 Example of Event Loop in Action

```
import asyncio

async def say_hello():
    await asyncio.sleep(1)
    print("Hello")

async def say_world():
    await asyncio.sleep(1)
    print("World")

async def main():
    await asyncio.gather(say_hello(), say_world())

asyncio.run(main())  # ← This starts the event loop
```

What Happens:
• asyncio.run(main()) → starts the event loop
• main() awaits two coroutines concurrently
• Event loop sleeps for 1 second, then prints both

⸻

🔁 How to Think About It

```
You Call…                                           What It Does
------------------------                            ---------------------------------------------------
asyncio.run(...)                                    Starts and manages the event loop automatically

await coro()                                        Pauses until the result is ready

asyncio.gather(...)                                 Runs multiple coroutines concurrently

await asyncio.sleep(n)                              Suspends for n seconds without blocking
```

🧠 Behind the Scenes

Python uses selectors under the hood (e.g., epoll, kqueue) to:
• Monitor file/network/socket events
• Schedule future tasks (via call_later, sleep)
• Resume paused coroutines efficiently

The event loop is single-threaded and non-blocking — meaning it can handle thousands of tasks as long as none of them blocks.

⸻

🚫 What Blocks the Event Loop?

Any sync or blocking call — like:
• time.sleep()
• open().read() (for big files)
• Long CPU work

Use:
• await asyncio.sleep()
• asyncio.to_thread(...)
• Or delegate CPU-heavy work to ProcessPoolExecutor

⸻

✅ TL;DR — Event Loop Summary

```
Concept                 Summary
----------------        -------------------------------------------------------------------
What it is              A task scheduler that runs and suspends coroutines

What it runs            Coroutines, tasks, futures, callbacks

When it runs            On asyncio.run(), or when manually started

How it switches         When a coroutine hits await, the loop picks the next ready task

Why it’s useful         Efficient concurrency without threads or blocking

```
