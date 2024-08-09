from typing import List, Tuple, Union


def seq_sum(sequence: Union[List, Tuple]) -> int:
    """
    Add your code here or call it from here   
    """
    total = 0
    for element in sequence:
        if isinstance(element, (list, tuple)):
            total += seq_sum(element)
        else:
            total += element
    return total
