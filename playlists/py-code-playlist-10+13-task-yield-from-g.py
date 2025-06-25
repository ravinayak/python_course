from collections import deque

def friends_upper():
    friends = deque(('Rolf', 'Jose', 'Rahul', 'Kim'))
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting}, how are you? {friend}')

def greet(g):
    g.send(None)
    while True:
        greeting = yield
        g.send(greeting)


def greet1(g):
    yield from g
    
g = greet(friends_upper())
g.send(None)
g.send('Hi')
g.send('Hello')
g.send('Hola Chicka')

g1 = greet1(friends_upper())
g1.send(None)
g1.send('Hi')
g1.send('Hello')
g1.send('Hola Chicka')