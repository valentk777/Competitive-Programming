from typing import List


def to_int(data: List[str]) -> List[int]:
    return list(map(int, data))


def read(filename: str = "input.txt") -> List[int]:
    with open(filename, "r") as f:
        return to_int(f.read().split())
