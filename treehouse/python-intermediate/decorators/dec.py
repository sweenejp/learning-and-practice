from functools import wraps


def outer():
    number = 5

    def inner():
        print(number)

    inner()


def apply(func, x, y):
    return func(x, y)


def add(x, y):
    return x + y


def close():
    x = 5

    def inner():
        print(x)
    return inner


def add_to_five(num):
    def inner():
        print(num + 5)
    return inner


def logme(func):
    import logging
    logging.basicConfig(level=logging.DEBUG)

    # @wraps puts docstrings and name and whatever else into func
    @wraps(func)
    def inner(*args, **kwargs):
        logging.debug("Called {} with args {} and kwargs {}".format(
            func.__name__, args, kwargs))
        return func(*args, **kwargs)
    return inner


@logme
def print_4():
    print(4)


@logme
def sub(x, y, switch=False):
    """Returns the difference between two numbers"""
    return x - y if not switch else y - x
