from typing import Dict
import time

# Dictionary to store execution times
execution_time: Dict[str, float] = {}


def time_decorator(fn):
    """
    Decorator function to measure execution time of decorated functions
    and store the time in `execution_time` dictionary.

    :param fn: Function to be decorated
    :return: Decorated function
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        execution_time[fn.__name__] = end_time - start_time
        return result

    return wrapper





