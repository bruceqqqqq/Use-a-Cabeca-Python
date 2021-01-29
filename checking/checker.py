from functools import wraps
from flask import session


def check_logged_in(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return 'YOU ARE NOT LOGGED IN!'

    return wrapper
