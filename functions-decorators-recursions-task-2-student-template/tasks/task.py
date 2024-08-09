from typing import Any, List


def linear_seq(sequence: List[Any]) -> List[Any]:
    """
    Flatten a nested sequence into a single list without nested sequences.

    :param sequence: A potentially nested list or tuple.
    :return: A flattened list containing all elements of the original sequence.
    """
    flattened = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            flattened.extend(linear_seq(item))
        else:
            flattened.append(item)
    return flattened
