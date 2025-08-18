import functools

users = [
    { 'username': 'John', 'level': 'admin' },
    { 'username': 'Cena', 'level': 'user' }
]

def third_level(access):
    def user_has_permission(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            '''
                This is a secure function
            '''
            if access and len(args) > 0:
                if args[0].get('level') == access:
                    return func(*args)
                else:
                    return None
        return secure_function
    
    return user_has_permission

@third_level('admin')
def my_function(user, user1):
    '''
        This is the document of my function
    '''
    return f'\nPassword for {user} is 1234, because we are using args, we also get 2nd positional argument {user1}'

@third_level('user')
def another():
    return 'Hi There!'

@third_level('invalid')
def level_invalid(user):
    return f'Invalid Function for {user}!'

x = third_level('admin')(my_function)
user_has_permissions_returned = third_level('admin')
my_secure_func = user_has_permissions_returned(my_function)

print(f'Name of function :: {my_function.__name__}')
print(f'\nInvoking password return function :: {my_function(users[0], users[1])}\n')
print(f'\nInvoking through explicit call of password return function :: {x(users[0], users[1])}')
print(f'\nInvoking through explicit call of password return function :: {my_secure_func(users[0], users[1])}')
print(f'\nHereby Doc function :: {my_function.__doc__}\n')
print(f'\nInvoking hi return function :: {another()}')
print(f'\nInvoking invalid return function :: {level_invalid(users[1])}')