def union(*args) -> set:
    """
    Return the union of all given sets, lists, or tuples.

    :param args: Any number of lists, tuples, or sets.
    :return: A set containing the union of all elements.
    """
    result = set()
    for arg in args:
        result.update(arg)
    return result

def intersect(*args) -> set:
    """
    Return the intersection of all given sets, lists, or tuples.

    :param args: Any number of lists, tuples, or sets.
    :return: A set containing the intersection of all elements.
    """
    if not args:
        return set()
    result = set(args[0])
    for arg in args[1:]:
        result.intersection_update(arg)
    return result

