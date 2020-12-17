from dataclasses import dataclass
from typing import List

import more_itertools as mit

from utils import read_lines


@dataclass
class Rule:
    name: str
    locations: List
    position: List


def to_rule(data: str) -> Rule:
    parts = data.split(": ")
    number_parts = parts[1].split(" or ")

    from_number_1, to_number_1 = map(int, number_parts[0].split("-"))
    from_number_2, to_number_2 = map(int, number_parts[1].split("-"))

    locations = [0 for _ in range(to_number_2 + 1)]
    for i in range(from_number_1, to_number_1 + 1):
        locations[i] = 1
    for i in range(from_number_2, to_number_2 + 1):
        locations[i] = 1
    return Rule(parts[0], locations, [])


def get_rules(data: List[str]) -> List[Rule]:
    return list(map(to_rule, data))


def get_tickets(data: List[str]) -> List[List[int]]:
    return list(map(lambda x: list(map(int, x.split(","))), data))


def convert_data():
    _rules, _my_ticket, _tickets = list(mit.split_at(input_data, pred=lambda x: x == ""))

    _rules = get_rules(_rules)
    _my_ticket = list(map(int, _my_ticket[1].split(",")))
    _tickets = get_tickets(_tickets[1:])

    return _rules, _my_ticket, _tickets


def get_locations_map(rules_list):
    locations = [0 for _ in range(10000)]
    for r in rules_list:
        for i in range(len(r.locations)):
            if r.locations[i] == 1:
                locations[i] = 1
    return locations


def get_valid_tickets(rules_list, tickets_list):
    locations = get_locations_map(rules_list)
    valid_tickets = []
    invalid_tickets = []

    for _ticket in tickets_list:
        valid = True
        for number in _ticket:
            if locations[number] == 0:
                invalid_tickets.append(number)
                valid = False
                break
        if valid:
            valid_tickets.append(_ticket)

    return valid_tickets, invalid_tickets


def get_rules_with_positions(grules):
    grules = grules.copy()
    final_rules = []
    i = 0

    while grules:
        rule = grules[i]

        if len(rule.position) == 1:
            final_rules.append(rule)
            grules.remove(rule)

            for rr in grules:
                if rule.position[0] in rr.position:
                    rr.position.remove(rule.position[0])
            i = 0
            continue
        i += 1

    return final_rules


def solve_1(invalid_tickets_list: List[List[int]]):
    print(sum(invalid_tickets_list))


def solve_2(lrules, lmy_ticket, lvalid_tickets):
    numbers_for_groups = list(map(list, zip(*reversed(lvalid_tickets))))

    for i in range(len(numbers_for_groups)):
        for rule in lrules:
            if all([rule.locations[g] == 1 for g in numbers_for_groups[i]]):
                rule.position.append(i)

    final_rules = get_rules_with_positions(lrules)
    departure_rules = filter(lambda x: x.name.startswith("departure"), final_rules)

    multi = 1
    for rule in departure_rules:
        multi *= lmy_ticket[rule.position[0]]

    print(multi)


if __name__ == "__main__":
    input_data = read_lines()
    rules, ticket, tickets = convert_data()
    valid_tickets, invalid_tickets = get_valid_tickets(rules, tickets)

    solve_1(invalid_tickets)
    solve_2(rules, ticket, valid_tickets)
