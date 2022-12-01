# ---------------------------------------------------------------------------------------
# URL    : https://adventofcode.com/2020/day/4
# Title  : Passport Processing
# Tags   : tag-adventofcode
# ---------------------------------------------------------------------------------------

# region --------------------------------------------Shared part--------------------------------------------------------

import math
import sys
from collections import defaultdict, Counter
from typing import List, Iterable

from utils import read_with_empty_lines


list_to_string = lambda _a: "".join(map(str, _a))
list_to_string_list = lambda _a: " ".join(map(str, _a))
_dp = lambda default_value: defaultdict(lambda: default_value)
fact = lambda number: math.factorial(number)
cnt = lambda _a: Counter(_a)


def lcm(a, b):
    return a * b // math.gcd(a, b)


def print_dp(_dict):
    for item in _dict.items():
        print(f"{item[0]} = {item[1]}")


MOD = 10 ** 9 + 7
INF = sys.maxsize
A = 911382323
M = 9999999999879998


# endregion

# -------------------------------------------------------Solution-------------------------------------------------------


def to_dict(data_to_convert) -> dict:
    return {x.split(':')[0]: x.split(':')[1] for x in data_to_convert}


def to_passports(data_to_convert) -> List[dict]:
    return list(map(to_dict, data_to_convert))


def is_valid(passport: dict) -> bool:
    return len(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] & passport.keys()) == 7


def get_all_valid_passports(passports_to_validate: Iterable[dict]) -> Iterable[dict]:
    return filter(is_valid, passports_to_validate)


def validate_byr(passports_to_validate: Iterable[dict]) -> Iterable[dict]:
    return filter(lambda x: 1920 <= int(x["byr"]) <= 2020, passports_to_validate)


def validate_iyr(passports_to_validate: Iterable[dict]) -> Iterable[dict]:
    return filter(lambda x: 2010 <= int(x["iyr"]) <= 2020, passports_to_validate)


def validate_eyr(passports_to_validate: Iterable[dict]) -> Iterable[dict]:
    return filter(lambda x: 2020 <= int(x["eyr"]) <= 2030, passports_to_validate)


def validate_hgt(passports_to_validate: Iterable[dict]) -> Iterable[dict]:
    def hgt_filter(passport):
        if passport["hgt"][-2:] == "cm":
            return 150 <= int(passport["hgt"][:-2]) <= 193
        elif passport["hgt"][-2:] == "in":
            return 59 <= int(passport["hgt"][:-2]) <= 76
        else:
            return False

    return filter(hgt_filter, passports_to_validate)


def validate_hcl(passports_to_validate: Iterable[dict]) -> Iterable[dict]:
    def hcl_filter(passport):
        if passport["hcl"][0] != "#":
            return False

        return len(passport["hcl"][1:]) == 6

    return filter(hcl_filter, passports_to_validate)


def validate_ecl(passports_to_validate: Iterable[dict]) -> Iterable[dict]:
    return filter(lambda x: x["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"], passports_to_validate)


def validate_pid(passports_to_validate: Iterable[dict]) -> Iterable[dict]:
    return filter(lambda x: len(x["pid"]) == 9, passports_to_validate)


def solve_1(data):
    print(len(list(get_all_valid_passports(data))))


def solve_2(data):
    all_valid = get_all_valid_passports(data)
    all_valid = validate_byr(all_valid)
    all_valid = validate_iyr(all_valid)
    all_valid = validate_eyr(all_valid)
    all_valid = validate_hgt(all_valid)
    all_valid = validate_hcl(all_valid)
    all_valid = validate_ecl(all_valid)
    all_valid = validate_pid(all_valid)
    print(len(list(all_valid)))


if __name__ == "__main__":
    input_data = read_with_empty_lines()
    input_data = to_passports(input_data)

    solve_1(input_data.copy())
    solve_2(input_data.copy())
