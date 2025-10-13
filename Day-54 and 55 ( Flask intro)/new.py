

def logging_decorator(f):
    def wrapper(*args):
        print(f"You called {f.__name__}{args}")
        print(f"It returned: {f(*args)}")
    return wrapper


@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)