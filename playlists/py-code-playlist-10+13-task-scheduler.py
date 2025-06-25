def countdown(n):
    while n > 0:
        yield
        print(f' Value of n :: {n}')
        n -= 1

tasks = [countdown(10), countdown(3), countdown(8)]

def task_scheduler():
    while len(tasks):
        task = tasks.pop(0)
        try:
            next(task)
            tasks.append(task)
        except StopIteration:
            pass

task_scheduler()

# If your generator’s logic doesn’t reach another yield before it ends, then next() raises StopIteration.
# In the 4th call, the value printed is 1, i decrements to 0, and the generator object is not able to reach
# another yield, since it exits the function, and hence StopIteration Error is raised
# 1st call does not print anything, because it gets suspended at yield
# 1st call is effectively primming the generator
# | Call | n Before | Yield? | Prints               | n After | Notes                         |
# |------|----------|--------|----------------------|---------|-------------------------------|
# | 1    | 3        | ✅     | ❌                   | 3       | Suspends at yield             |
# | 2    | 3        | ⏩     | "Value of n :: 3"    | 2       | Resumes, prints, decrements   |
# | 3    | 2        | ✅     | "Value of n :: 2"    | 1       | Normal step                   |
# | 4    | 1        | ✅     | "Value of n :: 1"    | 0       | Last value printed            |
# | 5    | 0        | ❌     | ❌                   | —       | Loop ends, StopIteration      |
# c3 = countdown(3)
# print('Calling next')
# next(c3)
# print('Calling next')
# next(c3)
# print('Calling next')
# next(c3)
# print('Calling next')
# next(c3)

