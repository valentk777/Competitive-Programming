import codecs
from typing import List


def to_int(data: List[str]) -> List[int]:
    return list(map(int, data))


def read_lines(filename: str = "input.txt") -> List[str]:
    return read(filename).split('\n')


def read(filename: str = "input.txt") -> str:
    with codecs.open(filename, 'U') as f:
        return f.read()


def read_with_empty_lines() -> List[List[str]]:
    input_data = read().split(2 * '\n')
    input_data = [x.split() for x in input_data]
    return input_data
