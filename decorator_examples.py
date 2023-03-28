
#This decorator adds logging functionality to the add function, printing out the function call and return value.
def log_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__} was called with arguments {args} and {kwargs}, and returned {result}")
        return result
    return wrapper

@log_decorator
def add(x, y):
    return x + y

print(add(2, 3))



# This decorator adds timing functionality to the slow_function function, printing out the time it took to run.
import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to run")
        return result
    return wrapper

@time_decorator
def slow_function():
    time.sleep(2)

slow_function()


# This decorator adds memoization functionality to the fibonacci function, caching the results of previous function calls to speed up future calls.
def memoize_decorator(func):
    memo = {}
    def wrapper(*args):
        if args in memo:
            return memo[args]
        result = func(*args)
        memo[args] = result
        return result
    return wrapper

@memoize_decorator
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))