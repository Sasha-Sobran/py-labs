"""
This module provides decorators for counting function arguments and limiting function calls.
"""

from Exceptions.exceptions import ToManyCallsException, NoSuchModeException
import logging


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
                raise ToManyCallsException()
            calls += 1
            return func(*args, **kwargs)

        return wrapper

    return decorator


def logged(exception, mode="console"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except exception as ex:
                if mode == "console":
                    logging.error(ex.log_message)
                elif mode == "file":
                    logging.basicConfig(filename='log.txt', level=logging.ERROR)
                    logging.error(ex.log_message)
                else:
                    raise NoSuchModeException() from ex

        return wrapper

    return decorator
