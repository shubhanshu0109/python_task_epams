from typing import Any, Tuple, List

def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    # TODO: Add your code here

    if len(lst) < 2:
        return []
    pairs = [(lst[i], lst[i + 1]) for i in range(len(lst) - 1)]
    return pairs
