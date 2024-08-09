from functools import wraps
from typing import Callable


def decorator_apply(lambda_func: Callable[[int], int]) -> Callable:
    """
    A decorator factory that takes a function (lambda) as input and returns a decorator.
    The decorator will modify the result of the decorated function using the lambda function.

    :param lambda_func: A function that takes one integer argument and returns an integer.
    :return: A decorator that applies the lambda function to the result of the decorated function.
    """

    def decorator(fn: Callable) -> Callable:
        @wraps(fn)
        def wrapper(*args, **kwargs):
            # Call the original function
            result = fn(*args, **kwargs)
            # Apply the lambda function to the result
            modified_result = lambda_func(result)
            return modified_result

        return wrapper

    return decorator


@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int) -> int:
    """
    Return the user ID passed as an argument.

    :param num: An integer representing a user ID.
    :return: The user ID.
    """
    return num


