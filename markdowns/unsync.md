### asyncio vs unsync - Thread Safety

1. When using pure asyncio, coroutines run within a single-threaded event loop,
   so it's safe to use asyncio.Queue, which is not thread-safe.

2. However, when using the unsync library, even @unsync async coroutines are
   executed in background threads (with their own event loops). This means
   multiple threads may access shared data like a queue.

3. Therefore, we use queue.Queue (which is thread-safe) instead of asyncio.Queue
   to safely share data between unsync-decorated coroutines and functions.

### unsync future object

generate_process_data().result() call.

⸻

🧩 What’s Happening in generate_process_data().result()?

1. @unsync Decorator

You’ve defined:

```
@unsync
async def generate_process_data():
    ...
```

This means:
• generate_process_data() returns an UnsyncFuture (not a coroutine).
• It wraps the async function and runs it in a background thread with its own event loop.

⸻

2. .result() on UnsyncFuture

UnsyncFuture is a custom object returned by the @unsync decorator.

```
future = generate_process_data()
future.result()
```

This:
• Blocks the main thread until the generate_process_data coroutine finishes.
• Then returns the final result (if any).
• Similar to calling .result() on a concurrent.futures.Future.

⸻

🔍 Why Not Just await generate_process_data()?

Because:
• generate_process_data() is not a coroutine, it’s an UnsyncFuture object.
• You can’t await it unless you’re inside another async function and the coroutine was not decorated with @unsync.

⸻

✅ Summary

```
Code                          What It Does
--------------------------    -------------------------------------------------------------------
1. @unsync async def f()         Wraps the async function to run in a background thread

2. f()                           Returns an UnsyncFuture

3. f().result()                  Blocks until the async function completes and gets the result

4. await f()                     ❌ Invalid – f is not an awaitable coroutine anymore
```

🧠 Final Example in Plain Terms

```
@unsync
async def foo():
    await asyncio.sleep(1)
    return 42

future = foo()          # This runs foo in background thread
result = future.result()  # Wait for foo to finish and get the result (42)
```
