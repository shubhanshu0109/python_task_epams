import math
from typing import Union

NumType = Union[int, float]

def some_expression_with_rounding(a: NumType, b: NumType) -> NumType:
  numerator = 12 * a + 25 * b
  denominator = 1 + a ** (2 ** b)
  result = numerator / denominator
  rounded_result = round(result, 2)

  return rounded_result

