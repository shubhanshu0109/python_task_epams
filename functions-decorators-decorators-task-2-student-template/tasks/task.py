import time
from functools import wraps


def log(fn):
    """
    A decorator that logs the function name, arguments, keyword arguments,
    and execution time to a log file.
    """

    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time

        # Prepare the log message
        arg_names = fn.__code__.co_varnames[:fn.__code__.co_argcount]
        arg_str = ", ".join(f"{name}={value}" for name, value in zip(arg_names, args))
        kwargs_str = ", ".join(f"{k}={v}" for k, v in kwargs.items())

        if arg_str and kwargs_str:
            log_message = f"{fn.__name__}; args: {arg_str}; kwargs: {kwargs_str}; execution time: {execution_time:.2f} sec.\n"
        elif arg_str:
            log_message = f"{fn.__name__}; args: {arg_str}; execution time: {execution_time:.2f} sec.\n"
        elif kwargs_str:
            log_message = f"{fn.__name__}; kwargs: {kwargs_str}; execution time: {execution_time:.2f} sec.\n"
        else:
            log_message = f"{fn.__name__}; execution time: {execution_time:.2f} sec.\n"

        # Write the log message to a file
        with open("log.txt", "a") as log_file:
            log_file.write(log_message)

        return result

    return wrapper


# Example usage
@log
def foo(a, b, c=0):
    time.sleep(0.1)
    return a + b + c


