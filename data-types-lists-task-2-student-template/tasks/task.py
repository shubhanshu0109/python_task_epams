from typing import Union, List

ListType = List[Union[int, str]]


def get_fizzbuzz_list(n: int) -> ListType:
    # TODO: Add your code here
    fizzbuzz_list: ListType = []
    for num in range(1, n + 1):
        if num % 3 == 0 and num % 5 == 0:
            fizzbuzz_list.append("FizzBuzz")
        elif num % 3 == 0:
            fizzbuzz_list.append("Fizz")
        elif num % 5 == 0:
            fizzbuzz_list.append("Buzz")
        else:
            fizzbuzz_list.append(num)
    return fizzbuzz_list