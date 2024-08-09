from typing import List


def foo(nums: List[int]) -> List[int]:
    # TODO: Add your code here
    n = len(nums)
    if n == 0:
        return []

    # Initialize output list
    result = [1] * n

    # Compute left products
    left_product = 1
    for i in range(n):
        result[i] *= left_product
        left_product *= nums[i]

    # Compute right products and combine with left products
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result