### create_task

Yes, asyncio.create_task() schedules the coroutine to start running on the event loop as soon as possible. It doesn't wait for you to await the task object.

Think of it this way:

Creating a Coroutine: my_coro = fetch_data() simply creates a coroutine object. It's like writing a recipe but not starting to cook.
Creating a Task: task = asyncio.create_task(my_coro) is like handing that recipe to a chef (the event loop) and saying, "Start working on this as soon as you have a free moment."
The chef will begin immediately, and if the recipe says "wait for 10 minutes," the chef won't just stand there. They will put the first dish in the oven and immediately start working on another recipe you've given them.

Awaiting the task (await task) is you waiting for the chef to tell you that specific dish is ready to serve. The cooking has been happening all along.
