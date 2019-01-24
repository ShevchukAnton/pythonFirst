# mandatory import to let this decorator know that it's a decorator though :)
import functools

from flask import session


def check_logged_in(func: 'function') -> object:
    # dont forget to decorate your decorator to let this decorator know that it's a decorator though :)
    @functools.wraps(func)
    # accepts any amount of any type arguments, as wwe don't know what arguments will be bypassed to our decorator
    def wrapper(*args, **kwargs):
        if 'logged_in' in session and session['logged_in']:
            # returns decorated function with arguments
            return func(*args, **kwargs)
        return 'You are NOT logged in'

    # returns function as an object without invoking it
    return wrapper
