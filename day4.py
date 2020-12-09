import re
from typing import TextIO

required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
valid_eye_colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}


def parse_passports(f: TextIO) -> list[dict[str, str]]:
    data = f.read()[:-1]
    data = data.split('\n\n')
    data = [re.split(r'[\n ]', string) for string in data]
    return [dict(string.split(':') for string in row) for row in data]


def has_required_fields(passport: dict[str, str]):
    global required_fields
    return set(passport.keys()).issuperset(required_fields)


def is_in_range(lb: int, ub: int, val: str):
    try:
        return lb <= int(val) < ub
    except ValueError:
        return False


def is_valid_birth_year(val: str):
    return is_in_range(1920, 2003, val)


def is_valid_issue_year(val: str):
    return is_in_range(2010, 2021, val)


def is_valid_expiration_year(val: str):
    return is_in_range(2020, 2031, val)


def is_valid_height(val: str):
    if val[-2:] == 'cm':
        lb = 150
        ub = 194
    elif val[-2:] == 'in':
        lb = 59
        ub = 77
    else:
        return False
    return is_in_range(lb, ub, val[:-2])


def is_valid_hair_color(val: str):
    return re.fullmatch(r'#[0-9a-f]{6}', val) is not None


def is_valid_eye_color(val: str):
    global valid_eye_colors
    return val in valid_eye_colors


def is_valid_passport_id(val: str):
    try:
        return len(val) == 9 and int(val)
    except ValueError:
        return False


def part1():
    with open('passports.txt') as f:
        passports = parse_passports(f)
    valid_passports = [passport for passport in passports if has_required_fields(passport)]
    return len(valid_passports)


def part2():
    with open('passports.txt') as f:
        passports = parse_passports(f)
    validators = {
        'byr': is_valid_birth_year,
        'iyr': is_valid_issue_year,
        'eyr': is_valid_expiration_year,
        'hgt': is_valid_height,
        'hcl': is_valid_hair_color,
        'ecl': is_valid_eye_color,
        'pid': is_valid_passport_id,
        'cid': lambda _: True,
    }

    valid_passports = []
    for passport in passports:
        is_valid = True
        if has_required_fields(passport):
            for k, v in passport.items():
                if not validators[k](v):
                    is_valid = False
                    break
        else:
            is_valid = False

        if is_valid:
            valid_passports.append(passport)
    return len(valid_passports)


if __name__ == '__main__':
    print(part1())
    print(part2())
