from typing import Tuple

def get_tuple(num: int) -> Tuple[int]:
    digits = tuple(int(digit) for digit in str(num))
    return digits
