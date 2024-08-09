from typing import Any, Dict, List, Set

def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    """
    Add your code here or call it from here   
    """
    unique_values = set()  # Initialize an empty set to store unique values

    for d in lst:  # Iterate through each dictionary in the list
        for value in d.values():  # Iterate through values in the dictionary
            unique_values.add(value)  # Add each value to the set

    return unique_values
