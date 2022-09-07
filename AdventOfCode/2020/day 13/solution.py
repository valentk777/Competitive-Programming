# -----------------------------------------------------------
# Notes  : tag-adventOfCode
# -----------------------------------------------------------


from dataclasses import dataclass
from functools import reduce
from itertools import combinations
from typing import List

from utils import read_lines

input_data = read_lines()


@dataclass
class Bus:
    id: int
    next_depart_time: int
    position: int


def generate_busses(data: List[str], current_time: int) -> List[Bus]:
    bus = []
    for i in range(len(data)):
        time = data[i]
        if time != "x":
            time = int(time)
            bus.append(Bus(time, ((current_time // time) + 1) * time, i))

    return bus


def generate_next(now: int, data: Bus):
    return now + data.id


def chinese_remainder(n, a):
    prod = reduce(lambda x, y: x * y, n)
    _sum = 0
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        _sum += a_i * mul_inv(p, n_i) * p
    return _sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1

    if b == 1:
        return 1

    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0

    if x1 < 0:
        x1 += b0

    return x1


def smallest_common(sequence_a_first_element, sequence_a_multiplier, sequence_b_first_element, sequence_b_multiplier):
    if sequence_a_first_element > sequence_b_first_element:
        sequence_a_first_element, sequence_b_first_element = sequence_b_first_element, sequence_a_first_element
        sequence_a_multiplier, sequence_b_multiplier = sequence_b_multiplier, sequence_a_multiplier

    possible_y = 0

    for possible_y in range(sequence_a_multiplier):
        first_term_diff = sequence_b_first_element - sequence_a_first_element

        if (first_term_diff % sequence_a_multiplier + possible_y * sequence_b_multiplier) % sequence_a_multiplier == 0:
            break

    if possible_y != sequence_a_multiplier:
        return sequence_b_first_element + possible_y * sequence_b_multiplier

    return -1


def solve_1(current_time: int, data: List[Bus]):
    data.sort(key=lambda x: x.next_depart_time)
    earliest = data[0]
    print(earliest.id * (earliest.next_depart_time - current_time))


# slow (using smallest common between two sequences
def solve_2_1(data: List[Bus]):
    for d in data:
        d.next_depart_time = generate_next(-d.position + d.id, d)

    while len(set(map(lambda x: x.next_depart_time, data))) != 1:
        for pair_1, pair_2 in combinations(data, 2):
            smallest = smallest_common(pair_1.next_depart_time, pair_1.id, pair_2.next_depart_time, pair_2.id)
            pair_1.next_depart_time, pair_2.next_depart_time = smallest, smallest
        print(data[0].next_depart_time)
    print(data[0].next_depart_time)


# fast (using Chinese Remainder Theorem)
def solve_2_2(data: List[Bus]):
    for d in data:
        d.next_depart_time = generate_next(-d.position + d.id, d)

    result = chinese_remainder(list(map(lambda x: x.id, data)), list(map(lambda x: x.next_depart_time, data)))
    print(result)


current = int(input_data[0])
busses = generate_busses(input_data[1].split(","), current)

solve_1(current, busses)
solve_2_2(busses)
