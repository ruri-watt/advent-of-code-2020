import operator

operations = {
    '+': operator.add,
    '*': operator.mul,
}


def calc(left: int, op, rest):
    if rest[0] == '(':
        i = index_of_matching_bracket(rest)
        lhs = op(left, calc(0, operator.add, rest[1:i]))
        if len(rest) - 1 == i:
            return lhs
        return calc(lhs, operations[rest[i + 1]], rest[i + 2:])
    rhs = int(rest[0])
    lhs = op(left, rhs)
    if len(rest) == 1:
        return lhs
    return calc(lhs, operations[rest[1]], rest[2:])


def index_of_matching_bracket(s, i=0):
    level = 1
    if s[i] == '(':
        while level != 0:
            i += 1
            if s[i] == '(':
                level += 1
            elif s[i] == ')':
                level -= 1
        return i
    else:
        while level != 0:
            i -= 1
            if s[i] == ')':
                level += 1
            elif s[i] == '(':
                level -= 1
        return i


def part1():
    with open('operation-order.txt') as f:
        return sum([calc(0, operator.add, line.replace(' ', '').replace('\n', '')) for line in f])


def part2():
    with open('operation-order.txt') as f:
        lines = [[c for c in line.replace(' ', '').replace('\n', '') if c] for line in f]
    for line in lines:
        i = 0
        while i < len(line):
            c = line[i]
            if c == '+':
                if line[i - 1] == ')':
                    left_insert_index = index_of_matching_bracket(line, i - 1)
                else:
                    left_insert_index = i - 1
                if line[i + 1] == '(':
                    right_insert_index = index_of_matching_bracket(line, i + 1) + 1
                else:
                    right_insert_index = i + 2
                line.insert(right_insert_index, ')')
                line.insert(left_insert_index, '(')
                i += 2
            else:
                i += 1
    return sum([calc(0, operator.add, line) for line in lines])


if __name__ == '__main__':
    print(part1())
    print(part2())
