import itertools


def part1():
    with open('expenses.txt') as f:
        expenses = [int(s) for s in f]
    solutions = [a * b for a, b in itertools.combinations(expenses, 2) if a + b == 2020]
    assert len(solutions) == 1
    return solutions[0]


def part2():
    with open('expenses.txt') as f:
        expenses = [int(s) for s in f]
    solutions = [a * b * c for a, b, c in itertools.combinations(expenses, 3) if a + b + c == 2020]
    assert len(solutions) == 1
    return solutions[0]


if __name__ == '__main__':
    print(part1())
    print(part2())
