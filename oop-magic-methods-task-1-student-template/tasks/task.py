from typing import List

class Counter:
    def __init__(self, values: List[int]):
        self.values = values

    def __add__(self, other: str) -> List[str]:
        if isinstance(other, str):
            return [f"{value} {other}" for value in self.values]
        return NotImplemented

