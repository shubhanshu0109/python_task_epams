
from typing import Dict

def combine_dicts(*args: Dict[str, int]) -> Dict[str, int]:
    """
    Combine multiple dictionaries into one, summing values for identical keys.

    :param args: Any number of dictionaries with keys as strings and values as integers.
    :return: A single dictionary with combined keys and summed values.
    """
    combined_dict = {}
    for dictionary in args:
        for key, value in dictionary.items():
            if key in combined_dict:
                combined_dict[key] += value
            else:
                combined_dict[key] = value
    return combined_dict