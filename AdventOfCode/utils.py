from typing import List


def to_int(data: str) -> List[int]:
    return list(map(int, data.split()))


def read(filename: str = "input.txt") -> str:
    with open(filename, "r") as f:
        return f.read()
