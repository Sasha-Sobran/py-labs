"""
This module provides decorators for counting function arguments and limiting function calls.
"""


def count_of_arguments(func):
    """
    Decorator that prints the number of arguments of a function.
    """

    def inner(*args, **kwargs):
        print(f"Number of arguments: {len(*args) + len(*kwargs)}")
        func(*args, **kwargs)

    return inner


def limit_calls(max_calls=3):
    """
    Decorator that limits the number of calls to a function.
    """

    def decorator(func):
        calls = 0

        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls >= max_calls:
                raise Exception("Too many calls")
            calls += 1
            return func(*args, **kwargs)

        return wrapper

    return decorator
