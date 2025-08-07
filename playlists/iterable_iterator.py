lst = [1, 2, 3]

for element in lst:
  print(f'Element :: {element}')
  
it = iter(lst)
print(f'Next :: {next(it)}')
print(f'Next :: {next(it)}')
print(f'Next :: {next(it)}')

try:
  print(f'Next :: {next(it)}')
except StopIteration:
  print('StopIteration encountered')
  
class ReusableCounterIterator:
  def __init__(self, limit):
    self.limit = limit
    self.start = 0
    
  def __iter__(self):
    return self
  
  def __next__(self):
   if self.start < self.limit:
     self.start += 1
     return self.start
   self.start = 0
   raise StopIteration
 
class Counter:
  def __init__(self, limit):
    self.limit = limit
    
  def __iter__(self):
    return ReusableCounterIterator(self.limit)
  
c = Counter(5)
for element in c:
  print(f'Element :: {element}')
  
c = Counter(5)
for element in c:
  print(f'Element :: {element}')

try:
  next(c)
except Exception as e:
  print(f'Exception occurred :: {e}')
  
d = ReusableCounterIterator(5)

for element in d:
  print(f'Element in ReusableCounterIterator :: {element}')
  
loop = 0
while loop < 5:
  print(f'Element obtained using Next :: {next(d)}')
  loop += 1
  
try:
  next(d)
except StopIteration:
  print('Stop Iteration Exception')
  
for element in d:
  print(f'Element in ReusableCounterIterator:: {element}')
  
class NonReusableCounterIterator:
  def __init__(self, limit):
    self.limit = limit
    self.start = 0
    
  def __iter__(self):
    return self
  
  def __next__(self):
   if self.start < self.limit:
     self.start += 1
     return self.start
   raise StopIteration
 
e = NonReusableCounterIterator(5)

for element in e:
  print(f'Element in NonReusableCounterIterator:: {element}')

# Nothing will be printed here
print('The following for loop will not print anything, since it is NonReusableIterator')
for element in e:
  print(f'Element in NonReusableCounterIterator:: {element}')
  
try:
  next(e)
except StopIteration:
  print('NonReusableCounterIterator cannot be reused, since all elements have been iterated over, next throws this error - StopIteration')
  
# A Generator is a special type of Iterator which automatically yields and is NonReusableIterator

def gen(limit):
  start = 0
  while start < limit:
    start += 1
    yield start
  
g = gen(5)
loop = 0
while loop < 5:
  loop += 1
  print(f'Next called on generator object :: {next(g)}')
  
try:
  next(g)
except StopIteration:
  print('Generator exhausted by calling next, raises StopIteration Error')
 