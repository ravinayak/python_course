##PrintVsList
`print(object)` uses `__str()__`, but `print([object])` uses `__repr()__`.

TypeError: can't send non-None value to a just-started generator
This error occurs because a generator function needs to be "primed" before you can send data into it.

When you create a generator object (e.g., g = greet()), the code inside the function has not yet run.
To start it, you must call next(g) or g.send(None). This runs the code up to the very first yield expression and then pauses the generator there.
Only after it's paused at a yield can it accept a value from a subsequent .send() call.
