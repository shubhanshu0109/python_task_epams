from typing import List


def split_by_index(s: str, indexes: List[int]) -> List[str]:
    start = 0
    parts = []
    for i in sorted(indexes):
        if i >= len(s) or i < start:
            continue
        parts.append(s[start:i])
        start = i
    parts.append(s[start:])
    return [p for p in parts if p]
