from functools import wraps


def validate(fn):
    """
    Decorator to validate arguments of the decorated function.
    All arguments must be between 0 and 256 inclusive.
    """

    @wraps(fn)
    def wrapper(*args, **kwargs):
        # Check if all arguments are within the valid range
        if all(isinstance(arg, int) and 0 <= arg <= 256 for arg in args):
            return fn(*args, **kwargs)
        else:
            return "Function call is not valid!"

    return wrapper


@validate
def set_pixel(x: int, y: int, z: int) -> str:
    """
    Set a pixel at coordinates (x, y) with the given color.
    All parameters must be integers between 0 and 256 inclusive.
    """
    return "Pixel created!"


