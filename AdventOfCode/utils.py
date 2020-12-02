from typing import List


def to_int(data:  List[str]) -> List[int]:
    return list(map(int, data))


def read(filename: str = "input.txt") -> List[str]:
    with open(filename, "r") as f:
        return f.read().split('\n')
