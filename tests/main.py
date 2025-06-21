def divide(x, y):
    if y == 0:
        raise ValueError('Division by 0 is not allowed')
    result = x / y
    print(f'Result of division of x by y is {result:.2f}')
    return result
    
def add(x, y):
    return x + y

def multiply(x, y):
    result = x * y
    return round(result + 1e-8, 2)

def subtract(x, y):
    result = x - y
    print(f'Result of x - y is {result:.2f}')
    return result