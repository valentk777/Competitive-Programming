import codecs
from typing import List


def to_int(data: List[str]) -> List[int]:
    return list(map(int, data))


def read_lines(filename: str = r"input.txt") -> List[str]:
    return list(filter(lambda x: x != "", read(filename).split('\n')))


def read(filename: str = r"input.txt") -> str:
    with codecs.open(filename) as f:
        return f.read()


def read_with_empty_lines() -> List[List[str]]:
    input_data = read().split(2 * '\n')
    input_data = [x.split() for x in input_data]
    return input_data


def read_with_empty_lines_int() -> List[List[int]]:
    input_data = read().split(2 * '\n')
    input_data = [to_int(x.split()) for x in input_data]
    return input_data
