# ---------------------------------------------------------------------------------------
# URL    : https://adventofcode.com/2022/day/15
# Title  : Beacon Exclusion Zone
# Tags   : tag-adventofcode, tag-not-pass
# ---------------------------------------------------------------------------------------

# region --------------------------------------------Shared part--------------------------------------------------------

import math
import sys
from collections import defaultdict, Counter

from utils import read_lines

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

def parse_data(data):
    def to_point(text):
        x, y = text.split(",")
        x = int(x.replace("x=", "").strip())
        y = int(y.replace("y=", "").strip())

        return x, y

    sensors = []
    beacons = []

    for line in data:
        line = line.replace("Sensor at ", "")
        line = line.replace("closest beacon is at ", "")
        sensor, beacon = line.split(":")
        sensors.append(to_point(sensor))
        beacons.append(to_point(beacon))

    return [sensors, beacons]


def solve_1(data) -> None:
    sensors, beacons = data
    n = len(sensors)

    # points only in concrete line like y = 10, y = 2000000 etc.
    target_y = 2000000
    zer_x = 50000000
    can_be_beacon_x = [True for _ in range(zer_x * 2 + 1)]

    for i in range(n):
        sensor = sensors[i]
        beacon = beacons[i]

        distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

        if sensor[1] - distance <= target_y <= sensor[1] + distance:
            if sensor[1] == target_y:
                for j in range(sensor[0] - distance, sensor[0] + distance + 1):
                    can_be_beacon_x[j + zer_x] = False
                continue

            _range = distance - abs(sensor[1] - target_y)

            for j in range(sensor[0] - _range, sensor[0] + _range + 1):
                can_be_beacon_x[j + zer_x] = False

        else:
            continue

        for beacon in beacons:
            if beacon[1] == target_y:
                can_be_beacon_x[beacon[0] + zer_x] = True

    print(can_be_beacon_x.count(False))


def solve_2(data) -> None:
    pass


if __name__ == "__main__":
    input_data = read_lines()

    solve_1(parse_data(input_data))
    solve_2(parse_data(input_data))
