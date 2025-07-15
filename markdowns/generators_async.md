```
Concept							✅ await?			    ✅ next()?					Notes
-------------					-------------		    -------------				  ------------

1. def + yield						❌					✅							Regular generators

2. async def + await				✅					❌							Regular coroutines

3. async def + yield				❌					✅ via async for				Async generators

4. __await__() object				✅					✅ if it’s a generator		Custom awaitables
```

✅ 1. def + yield

A regular generator (synchronous). You can next() it, but you can’t await it.

```
def gen():
    yield "hello"
    yield "world"

g = gen()
print(next(g))  # ✅ "hello"
print(next(g))  # ✅ "world"

# await g  ❌ TypeError: cannot 'await' a generator object

```

✅ 2. async def + await

A coroutine function. You must use await, but you can’t next() it.

```
import asyncio

async def say_hello():
    return "Hello Async"

async def main():
    result = await say_hello()  # ✅ works
    print(result)

asyncio.run(main())

# say_hello() is a coroutine
# next(say_hello())  ❌ TypeError

```

✅ 3. async def + yield

This defines an async generator. You can’t await it, but you can iterate with async for.

```
import asyncio

async def async_gen():
    for i in range(3):
        yield i  # ✅ allowed in async generators

async def main():
    async for val in async_gen():  # ✅ works
        print(val)

asyncio.run(main())

# await async_gen() ❌ TypeError: can't be awaited
# next(async_gen()) ❌ TypeError

```

✅ 4. Object with **await**()

Custom object that is awaitable. This can be await-ed and sometimes also next()-ed.

```
class CustomAwaitable:
    def __await__(self):
        print("Inside __await__")
        yield  # pause here
        return "Done!"

async def main():
    result = await CustomAwaitable()  # ✅ Yes, works
    print(result)

asyncio.run(main())

# Technically, you could also do:
g = CustomAwaitable().__await__()
print(next(g))  # ✅ works because __await__ returns a generator

```

A coroutine is a special kind of function in Python that can:
• pause its execution at a certain point,
• wait for input or other events,
• and then resume from where it left off.

They are used to write non-blocking, asynchronous, and cooperative multitasking code in a clean and readable way.

⸻

🧠 Simple Definition:

A coroutine is like a function that can pause, resume, and receive values, making it perfect for concurrent programming without threads.

🧪 Example 1: Basic Generator-as-Coroutine

```
def greeter():
    name = yield "What's your name?"
    yield f"Hello, {name}!"

g = greeter()
print(next(g))        # → "What's your name?"
print(g.send("Alice"))  # → "Hello, Alice!"

```

Here:
• yield pauses the function and optionally receives data back via .send(...).
• This is a “generator-based coroutine”.

⚙️ Coroutine vs Generator

```
Feature						Generator (def + yield)							Coroutine (async def)
--------------				------------------------------					------------------------------

1. Keyword						yield											await, async def

2. Resume with					next(), .send()									await, event loop

3. Use case						Data pipelines, lazy iteration					Async I/O, concurrency

4. Syntax						Synchronous										Asynchronous
```

🧪 Example 2: Async Coroutine (Modern Python)

```
import asyncio

async def download():
    await asyncio.sleep(1)
    return "Download complete"

async def main():
    result = await download()
    print(result)

asyncio.run(main())
```

Here:
• async def defines a coroutine function.
• await pauses until the awaited task completes (e.g., network delay, file read).

⸻

✅ Use Cases
• Network I/O: HTTP requests, WebSocket handling
• File I/O: reading large files asynchronously
• Cooperative multitasking: doing many things without threads
• Pipelines: coroutines that push/pull data

```
class CustomAwaitable:
    def __await__(self):
        print("Inside __await__")
        yield  # pause here
        return "Done!"

async def main():
    result = await CustomAwaitable()
    print(result)

asyncio.run(main())
```

✅ Output

```
Inside __await__
Done!
```

❓ Why Does This Work?

✳️ Python allows any object with a **await**() method to be await-ed.

That’s not an exception — it’s part of the official awaitable protocol.

According to PEP 492 (async/await), an object is awaitable if:
• It is a coroutine object, OR
• It has a **await**() method that returns an iterator

⸻

🔍 Let’s Look at This Line:

```
await CustomAwaitable()
```

Here’s what Python internally does: 1. Calls CustomAwaitable().**await**() → this returns a generator. 2. That generator is driven by the event loop (asyncio.run()), as if by repeated next() calls. 3. The yield inside the generator causes it to pause. 4. When the generator is complete, the return value ("Done!") is returned from await.

⸻

✅ What Makes This Legitimate?

Because the **await**() method returns a generator, and generators can be used in an async context if they’re returned by **await**, it is completely legal to use this as a custom awaitable.

This allows developers to define their own awaitable behaviors — useful in async frameworks, mocking, or custom scheduling.

⸻

✅ Confirming the Type

```
obj = CustomAwaitable()
print(hasattr(obj, '__await__'))  # True
print(type(obj.__await__()))      # <class 'generator'>
```

🧪 Using It Manually

You can drive it manually too:

```
g = CustomAwaitable().__await__()
print(next(g))   # None (yielded)
# print(next(g))  # StopIteration: Done!
```

🧠 So Is This an Exception?
• Yes, it’s unusual: Most things you await are coroutine functions.
• No, it’s not a hack or unintended: Python intentionally supports this via the **await**() protocol.

✅ TL;DR

```
Question												Answer
-------------------										-------------------

1. Can we await this?									✅ Yes — because it defines __await__() that returns a generator

2. Is this common?										❌ Rare in real-world apps — mostly in advanced frameworks

3. Is it an exception?									❌ No — it follows Python’s async protocol (__await__)

4. What’s the output?									Inside __await__, then Done!

5. Is the generator in __await__() automatically run?	✅ Yes — by the event loop

```

### These concepts — generator, iterator, and iterable — are closely related but not the same

✅ Short Summary

```

Term			Is it Iterable?		 Is it Iterator?		  Can use for loop?		Can use next()?

1. Iterable		✅ Yes			    ❌ Not necessarily		✅ Yes				 ❌ No (unless it’s also an iterator)

2. Iterator		✅ Yes				✅ Yes					✅ Yes				 ✅ Yes

3. Generator	✅ Yes				✅ Yes					✅ Yes				 ✅ Yes

```

🧠 Definitions

1. Iterable

An object that can be looped over (e.g., for x in obj).
✅ Must implement **iter**(), which returns an iterator.

📌 Examples: list, tuple, dict, str, generator, custom classes with **iter**.

```
lst = [1, 2, 3]
for i in lst:
    print(i)
```

You can get an iterator from it:

```
it = iter(lst)  # calls lst.__iter__()
```

2. Iterator

An object that produces values one at a time using **next**().

✅ Must implement both:
• **iter**() → returns self
• **next**() → returns the next item (raises StopIteration at the end)

```
it = iter([1, 2, 3])  # this is an iterator
print(next(it))  # 1
print(next(it))  # 2
```

3. Generator

A special kind of iterator created using a function with yield.

✅ Automatically:
• Implements **iter**() and **next**()
• Maintains internal state between calls

```
def my_gen():
    yield 1
    yield 2
    yield 3

g = my_gen()        # g is a generator (and also an iterator)
print(next(g))      # 1
print(next(g))      # 2
```

🔍 Key Differences

```

Feature						Iterable						Iterator
------------------			------------------				------------------

1. Used in for				✅ Yes							✅ Yes

2. Has __iter__()			✅ Yes							✅ Yes

3. Has __next__()			❌ Not required					✅ Yes

4. Can be reused			✅ Usually (e.g. list)			❌ No — exhausted after use

5. Needs iter()				✅ Yes							❌ Already ready
```

🧪 Examples to Compare

A. Iterable but Not Iterator

```
lst = [1, 2, 3]          # list is iterable
it = iter(lst)           # this is now an iterator

print(hasattr(lst, '__next__'))  # False
print(hasattr(it, '__next__'))   # True
```

B. Generator is Iterator & Iterable

```
def gen():
    yield 1

g = gen()

print(hasattr(g, '__iter__'))  # True
print(hasattr(g, '__next__'))  # True
```

✅ Summary

```
Type						Reusable?						 Notes
----------------			----------------				 ----------------

1. List, Tuple				✅ Yes							Can re-iterate many times

2. Generator				❌ No							One-shot, must recreate

3. Iterator					❌ No							Usually one-shot
```

### Explanation of the following Code which uses await with a generator object

```
from collections import deque
from types import coroutine

friends = deque(['Ram', 'Sita', 'Laxman', 'Shatrughan', 'Bharat', 'Hanuman'])

@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')

async def greet(g):
    await g

greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')
greeter.send('Hi')
greeter.send('Hey')
greeter.send('What')
greeter.send('Why')
```

How is a generator (via @coroutine) being awaited in await g?

The short answer is:

Because @coroutine turns a generator into an awaitable coroutine — by giving it a **await**() method under the hood.

⸻

🧠 Let’s unpack this step by step

✅ Code Recap:

```
from collections import deque
from types import coroutine

friends = deque(['Ram', 'Sita', 'Laxman', 'Shatrughan', 'Bharat', 'Hanuman'])

@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')
```

You’re using:

```
@coroutine
```

from:

```
from types import coroutine
```

from types import coroutine

```
This decorator transforms a generator-based coroutine into something that can be used with await.
```

⸻

✅ What does @coroutine do?

It marks the generator function so that it behaves like an awaitable object — that is:
• It adds a **await**() method to the generator object.
• This makes it legal to use with await.

So this line:

```
await g
```

works, because:
• g is the generator returned by friend_upper()
• @coroutine makes g.**await**() available
• Python’s event loop knows how to drive **await**() step-by-step

This is how asyncio used to work before async def/await syntax was introduced (i.e., Python 3.4 and earlier Python 3.5 styles).

⸻

🔬 Under the Hood: What’s Happening

```

@coroutine
def friend_upper():
...

```

Becomes:

```
def friend_upper():
...
friend_upper = types.coroutine(friend_upper)

```

Internally, this creates a generator object with a . **await**() method that delegates to the generator itself using yield from.

⸻

✅ What Happens During Execution?

```

greeter = greet(friend_upper())

```

    •	friend_upper() returns a generator (but marked as awaitable)
    •	greet() is a coroutine that awaits this generator

```

greeter.send('Hello') # greeting = 'Hello'

```

Causes:

```

print(f'{greeting} {friend}')

```

✅ No, you cannot use await in a function that is not declared with async def.

Trying to use await in a regular def function will result in a SyntaxError.

⸻

```
def regular_function():
    await some_coroutine()  # ❌ Invalid

# SyntaxError: 'await' outside async function
```

Python requires that any use of await must be inside an async def function — this is enforced at the syntax level by the parser.

⸻

✅ Correct Usage

```
async def my_async_function():
    await some_coroutine()
```

And then you run it via:

```
import asyncio
asyncio.run(my_async_function())
```

🧠 Why This Restriction Exists
• await only makes sense in the context of a coroutine.
• The event loop must manage the paused/resumed state of the function, which requires it to be async def.
• Regular def functions return values immediately and can’t suspend execution.

⸻

✅ TL;DR

```
Question                                                       Answer
--------------                                                 --------------
1. Can you use await inside a regular def function?            ❌ No — it’s a syntax error
2. What kind of function can use await?                        ✅ Only async def functions
3. Why?                                                        Because only async def functions are coroutines
                                                               that can pause/resume under control of the event loop
```

#### without create_task, can we run multiple coroutines at the same time, meaning if we simply await 2 co routines without creating tasks for them, will they run concurrerntly?

Great question — you’re digging into a key concept in Python’s asyncio: what makes coroutines run concurrently?

⸻

🔑 Short Answer

❌ No, if you await two coroutines sequentially without using create_task() or gather(), they will not run concurrently.

They will run one after the other, just like synchronous code — because await waits for the first to finish before moving to the next.

```
import asyncio

async def task1():
    print("Start task1")
    await asyncio.sleep(1)
    print("End task1")

async def task2():
    print("Start task2")
    await asyncio.sleep(1)
    print("End task2")

async def main():
    await task1()  # 👈 waits until task1 is fully done
    await task2()  # 👈 starts only after task1 is done

asyncio.run(main())
```

Output:

```
Start task1
End task1
Start task2
End task2
```

⏱ Total time: ~2 seconds → Sequential execution

Concurrent Execution Without create_task: Use asyncio.gather

```
async def main():
    await asyncio.gather(task1(), task2())  # ✅ runs concurrently

# OR, more explicitly:
# t1 = task1()
# t2 = task2()
# await asyncio.gather(t1, t2)
```

Output:

```
Start task1
Start task2
End task1
End task2
```

⏱ Total time: ~1 second → Concurrent execution

✅ Or Use asyncio.create_task (Explicit task scheduling)

```
async def main():
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())
    await t1
    await t2
```

✅ TL;DR

```

Pattern                                         Concurrent?          Notes
----------------------------------------        --------------      ------------------
1. await task1(); await task2()                    ❌ No                Runs one after the other

2. await asyncio.gather(task1(), task2())          ✅ Yes               Best for launching coroutines together

3. create_task + await                             ✅ Yes               Lower-level, used for long-lived tasks


```

🧠 Final Note:

```
await = wait for one thing

asyncio.gather / create_task = start multiple things, then await them together

```

### Let’s walk through a complete, detailed example of using the unsync library to run:

    •	Synchronous functions
    •	Asynchronous coroutines
    •	CPU-bound functions (processes)
    •	All in parallel

We’ll show:
• How to declare each type
• What each returns (UnsyncFuture)
• How to access the results
• What’s happening under the hood

🧠 Overview

```
Type of Task                    Decorator Syntax                Backed by                   Returns
--------------------------      --------------------------      --------------------        ----------------

Sync I/O-bound (default)        @unsync                         ThreadPoolExecutor          UnsyncFuture
CPU-bound (heavy compute)       @unsync(process=True)           ProcessPoolExecutor         UnsyncFuture
Async coroutine                 @unsync on async def            asyncio event loop          UnsyncFuture

```

✅ Step 2: Full Example

```
from unsync import unsync
import time
import asyncio
import math

# --- Threaded: I/O-style sleep ---
@unsync
def sleep_task(name):
    time.sleep(1)
    return f"Done sleeping: {name}"

# --- Async: asyncio-style task ---
@unsync
async def async_task(name):
    await asyncio.sleep(1)
    return f"Done async: {name}"

# --- Process: CPU-bound task ---
@unsync(process=True)
def cpu_task(x):
    # Simulate CPU-intensive operation
    return f"CPU result: sqrt({x}) = {math.sqrt(x)}"

# --- Run all tasks together ---
def main():
    futures = [
        sleep_task("Threaded"),       # Threaded function
        async_task("Async"),          # Async coroutine
        cpu_task(1000000),            # CPU-bound process
    ]

    # These are all UnsyncFuture objects
    for f in futures:
        print(f"Type: {type(f)}")     # Shows <class 'unsync.future.UnsyncFuture'>

    # Wait for all to complete and collect results
    results = [f.result() for f in futures]
    print("\nResults:")
    for r in results:
        print(r)

if __name__ == '__main__':
    main()
```

✅ Output

```
Type: <class 'unsync.future.UnsyncFuture'>
Type: <class 'unsync.future.UnsyncFuture'>
Type: <class 'unsync.future.UnsyncFuture'>

Results:
Done sleeping: Threaded
Done async: Async
CPU result: sqrt(1000000) = 1000.0
```

✔️ Each task runs concurrently:
• The sleep_task runs in a thread.
• The async_task runs on the async event loop.
• The cpu_task runs in a separate process.

They all return an UnsyncFuture, which supports:

```
Method / Property                                   Meaning
-----------------------------                       -----------------------------------------
1. .result()                                        Wait and return the result (blocking)

2. .done()                                          True if completed

3. .exception()                                     Returns exception if raised

4. .add_done_callback(fn)                           Call when future completes

```

🔍 Under the Hood

@unsync
• On def: runs in ThreadPoolExecutor
• On async def: runs on asyncio event loop
• On def with process=True: runs in ProcessPoolExecutor

🧠 Bonus: Non-blocking Access with .add_done_callback

```
f = sleep_task("Ram")
f.add_done_callback(lambda fut: print("Callback:", fut.result()))
```

You can even use fut.result(timeout=...) to control blocking behavior.

✅ Summary Table of Unsync Usage

```

What You Want                                   Decorator                       Returns                 Runs In
-----------------------------------------       ----------------------          -----------------       ----------------------
1. Async coroutine                              @unsync on async def            UnsyncFuture            asyncio event loop

2. I/O-style blocking (e.g., time.sleep)        @unsync on def                  UnsyncFuture            ThreadPoolExecutor

3. Heavy computation                            @unsync(process=True)           UnsyncFuture            ProcessPoolExecutor

```

✅ TL;DR

• unsync simplifies concurrency without managing threads, event loops, or futures manually.
• All functions return UnsyncFuture regardless of backend.
• .result() blocks until completion and returns the result.
• All tasks run concurrently, giving performance and simplicity.

### Can we prime a coroutine by using next()?

✅ Yes — but only for regular generator-based coroutines, not async def coroutines.

Let’s break it down very clearly, because it depends entirely on the kind of coroutine you’re talking about:

✅ 1. Generator-based coroutine (@coroutine + yield)

Yes, you can prime it using next() — because it’s still a generator under the hood.

```
from types import coroutine

@coroutine
def gen_coro():
    print("Primed")
    yield "Paused here"

g = gen_coro()

print(next(g))  # ✅ works: "Primed" then yields "Paused here"
```

🔍 Why this works:
• @coroutine transforms a generator into an awaitable coroutine, but it’s still a generator object.
• So next(g) and g.send(...) still work.
• await g also works.

❌ 2. Native coroutine (async def)

❌ No, you cannot use next() on a coroutine defined with async def.

```
async def native_coro():
    print("Inside")
    return 42

c = native_coro()

next(c)  # ❌ TypeError: 'coroutine' object is not an iterator
```

🔍 Why this fails:
• Native coroutines (created with async def) are not iterators.
• They must be awaited (await c) or wrapped in an asyncio task.

🧠 Summary Table

```
Type of Function                Can you next() it?              Can you await it?
-----------------               ----------------------          --------------------------

1. def + yield                  ✅ Yes                           ❌ No

2. @coroutine + yield           ✅ Yes                          ✅ Yes

3. async def                    ❌ No                           ✅ Yes

4. async def + yield            ❌ No (not iterable)            ❌ No (async for) only

```

✅ Final Verdict

You can prime a coroutine with next() only if it’s a generator-based coroutine, such as one decorated with @coroutine.
You cannot use next() on a coroutine created via async def.

#### so for most generators, we can use next/send interchangeably ?

Excellent question — and the short answer is:

✅ Yes, for most generators, you can use .next() and .send(None) interchangeably — but there are important nuances you should know.

Let’s break it down clearly and precisely:

⸻

✅ When next() and send(None) Are Equivalent

🔁 Basic generator:

```
def my_gen():
    yield "step 1"
    yield "step 2"

g = my_gen()

print(next(g))        # ✅ "step 1"
print(g.send(None))   # ✅ "step 2" — works like next()
```

📌 send(None) is exactly the same as next() when:
• The generator is waiting at a bare yield
• You don’t want to inject any actual data

⸻

❗ When next() and send(None) Are Not Interchangeable

🔸 Case 1: First call to a generator with yield = (expression)

```
def my_gen():
    name = yield "What's your name?"
    yield f"Hello, {name}"

g = my_gen()

print(next(g))         # ✅ primes the generator, yields "What's your name?"
print(g.send("Alice")) # ✅ sends "Alice" into the generator
```

❌ But this will fail:

```
g = my_gen()
g.send("Alice")  # ❌ TypeError: can't send non-None value to a just-started generator
```

You must prime the generator first using next() or send(None).

⸻

🔸 Case 2: When you want to inject a value into the generator

Then send(...) is the only option:

```
def echo():
    while True:
        val = yield
        print(f"Received: {val}")

g = echo()
next(g)         # ✅ primes to first `yield`
g.send("Hello") # ✅ sends "Hello" into the generator
```

Calling next(g) here again would just send None, which isn’t useful if you’re expecting real data.

⸻

🧠 Summary Table

```
Use Case                                Use next()                  Use send(None)              Use send(value)

1. Prime a new generator                ✅ Yes                      ✅ Yes                      ❌ No

2. Resume at a bare yield               ✅ Yes                      ✅ Yes                      ⚠️ Only if value is None

3. Pass value to yield expression       ❌ No                       ❌ No                       ✅ Yes

```

✅ TL;DR
• next() is shorthand for send(None)
• You must use next() or send(None) to prime a generator (first step)
• Use send(value) only after priming, when the generator is paused at name = yield
• ⚠️ Never use send(value) on a just-started generator — you’ll get a TypeError
