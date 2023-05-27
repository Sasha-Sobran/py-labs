import inspect


def count_of_arguments(func):
    def inner(*args, **kwargs):
        print(f"Number of arguments: {len(inspect.signature(func).parameters)}")
        func(*args, **kwargs)

    return inner


def limit_calls(max_calls=3):
    def decorator(func):
        calls = 0

        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls < max_calls:
                return func(*args, **kwargs)
            else:
                raise Exception("Too many calls")

        return wrapper

    return decorator
