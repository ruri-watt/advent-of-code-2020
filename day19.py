import itertools

solution_cache = dict()


def divisions(length, nr_parts):
    return ((0, *comb, length) for comb in itertools.combinations(range(1, length), nr_parts - 1))


def check(input_string, rules, i=0):
    rule = rules[i]
    if isinstance(rule, str):
        return input_string == rule
    try:
        return solution_cache[(i, input_string)]
    except KeyError:
        if min([len(r) for r in rule]) > len(input_string):
            solution_cache[(i, input_string)] = False
            return False
        for rule_nrs in rule:
            for division in divisions(len(input_string), len(rule_nrs)):
                if all([check(input_string[division[i]:division[i + 1]], rules, rule_nrs[i]) for i in
                        range(len(rule_nrs))]):
                    solution_cache[(i, input_string)] = True
                    return True
        solution_cache[(i, input_string)] = False
        return False


def get_degree(type, rule_nr, rules):
    if isinstance(rules[rule_nr], str):
        return 1
    rule = rules[rule_nr]
    return type([sum([get_degree(type, n, rules) for n in ns]) for ns in rule])


def part1():
    rules = dict()
    with open('monster-messages.txt') as f:
        for line in f:
            if line == '\n':
                break
            index, rule = line.split(': ')
            if rule[0] == '"':
                rules[int(index)] = rule[1]
            else:
                rules[int(index)] = [list(map(int, pair.split(' '))) for pair in line.split(': ')[1].split(' | ')]
        max_length = get_degree(max, 0, rules)
        min_length = get_degree(min, 0, rules)
        print(f'{min_length}, {max_length}')
        nr_matched = 0
        for line in f:
            if len(line[:-1]) < min_length or len(line[:-1]) > max_length:
                print(f'{line[:-1]} failed')
            else:
                if check(line[:-1], rules):
                    nr_matched += 1
                    print(f'{line[:-1]} passed')
                else:
                    print(f'{line[:-1]} failed')
        return nr_matched


def part2():
    rules = dict()
    with open('monster-messages.txt') as f:
        for line in f:
            if line == '\n':
                break
            index, rule = line.split(': ')
            if rule[0] == '"':
                rules[int(index)] = rule[1]
            else:
                rules[int(index)] = [list(map(int, pair.split(' '))) for pair in line.split(': ')[1].split(' | ')]
        rules[8] = [[42], [42, 8]]
        rules[11] = [[42, 31], [42, 11, 31]]
        nr_matched = 0
        for line in f:
            if check(line[:-1], rules):
                nr_matched += 1
                print(f'{line[:-1]} passed')
            else:
                print(f'{line[:-1]} failed')
        return nr_matched


if __name__ == '__main__':
    print(part1())
    print(part2())
