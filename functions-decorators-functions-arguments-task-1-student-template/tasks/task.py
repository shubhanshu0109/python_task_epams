from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]

def query(data: DataType, selector: ModifierFunc, *filters: ModifierFunc) -> DataType:
    """
    Query data with column selection and filters.

    :param data: List of dictionaries with columns and values.
    :param selector: Result of `select` function call.
    :param filters: Any number of results of `field_filter` function calls.
    :return: Filtered data.
    """
    for f in filters:
        data = f(data)
    return selector(data)

def select(*columns: str) -> ModifierFunc:
    """Return function that selects only specific columns from dataset."""
    def selector(data: DataType) -> DataType:
        return [{col: d[col] for col in columns if col in d} for d in data]
    return selector

def field_filter(column: str, *values: Any) -> ModifierFunc:
    """Return function that filters specific column to be one of `values`."""
    def filter_func(data: DataType) -> DataType:
        return [d for d in data if d.get(column) in values]
    return filter_func

def test_query():
    friends = [
        {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'},
        {'name': 'Emily', 'gender': 'female', 'sport': 'Volleyball'},
    ]
    value = query(
        friends,
        select('name', 'gender', 'sport'),
        field_filter('sport', 'Basketball', 'Volleyball'),
        field_filter('gender', 'male'),
    )
    assert [{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'}] == value

if __name__ == "__main__":
    test_query()

