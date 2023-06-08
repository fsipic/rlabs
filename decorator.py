from functools import wraps
from datetime import datetime, timedelta


def cache_decorator(func, call_limit=10, minutes=5):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        signature = (func.__name__, args, tuple(kwargs.items()))
        current_time = datetime.now()

        if signature in cache:
            expiry_time, call_count, result = cache[signature]

            if current_time >= expiry_time or call_count >= call_limit:
                result = func(*args, **kwargs)
                cache[signature] = (current_time + timedelta(minutes), 1, result)
            else:
                cache[signature] = (expiry_time, call_count + 1, result)
        else:
            result = func(*args, **kwargs)
            cache[signature] = (current_time + timedelta(minutes), 1, result)
        return result

    return wrapper
