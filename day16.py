import re
from pprint import pprint
from typing import List, Iterable

import numpy as np


class Field:
    def __init__(self, name: str, valid_ranges: List[range]):
        self.name = name
        self.valid_ranges = valid_ranges

    def is_valid(self, number):
        return any(number in r for r in self.valid_ranges)


def parse_field(s: str):
    name, limits_def = s.split(':')
    limits = [int(limit) for limit in re.findall(r'([0-9]+)', limits_def)]
    ranges = [range(limits[i], limits[i + 1] + 1) for i in range(0, len(limits), 2)]
    return Field(name, ranges)


def is_invalid(number: int, fields: Iterable[Field]):
    return all(not f.is_valid(number) for f in fields)


def is_valid_ticket(ticket: Iterable[int], fields: Iterable[Field]):
    return not any(is_invalid(n, fields) for n in ticket)


def part1():
    fields = dict()
    error_rate = 0
    with open('ticket-translation.txt') as f:
        for line in f:
            if line == '\n':
                break
            field = parse_field(line)
            fields[field.name] = field
        while f.readline() != 'nearby tickets:\n':
            pass
        for line in f:
            ticket_numbers = [int(n) for n in line.split(',')]
            error_rate += sum([n for n in ticket_numbers if is_invalid(n, fields.values())])
    return error_rate


def part2():
    field_by_name = dict()

    with open('ticket-translation.txt') as f:
        for line in f:
            if line == '\n':
                break
            field = parse_field(line)
            field_by_name[field.name] = field

        possible_field_names = [set(field_by_name.keys()) for _ in range(len(field_by_name))]

        while f.readline() != 'your ticket:\n':
            pass
        line = f.readline()
        my_ticket = [int(n) for n in line.split(',')]

        while f.readline() != 'nearby tickets:\n':
            pass
        nearby_tickets = [[int(n) for n in line.split(',')] for line in f]

    valid_nearby_tickets = [t for t in nearby_tickets if is_valid_ticket(t, field_by_name.values())]

    for ticket in valid_nearby_tickets:
        for field_value, possible_names in zip(ticket, possible_field_names):
            impossible_names = set(n for n in possible_names if not field_by_name[n].is_valid(field_value))
            possible_names -= impossible_names

    while any(len(s) > 1 for s in possible_field_names):
        identified = [s for s in possible_field_names if len(s) == 1]
        undetermined = [s for s in possible_field_names if len(s) > 1]
        for u in undetermined:
            for i in identified:
                u -= i

    indices = [i for i, name in enumerate(possible_field_names) if name.pop().startswith('departure')]
    return np.prod([my_ticket[i] for i in indices])


if __name__ == '__main__':
    print(part1())
    print(part2())
