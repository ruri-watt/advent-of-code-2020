import itertools


def part1():
    with open('xmas-data.txt') as f:
        numbers = [int(line) for line in f]

    def is_valid(index):
        if index < 25:
            return True
        for i, j in itertools.combinations(numbers[index - 25:index], 2):
            if i + j == numbers[index]:
                return True
        return False

    return next(nr for i, nr in enumerate(numbers) if not is_valid(i))


def part2():
    target_number = part1()
    with open('xmas-data.txt') as f:
        numbers = [int(line) for line in f]
    slices = (slice(i, j) for i in range(len(numbers)) for j in range(i + 2, len(numbers)))
    solution_numbers = next(numbers[s] for s in slices if sum(numbers[s]) == target_number)
    return min(solution_numbers) + max(solution_numbers)


if __name__ == '__main__':
    print(part1())
    print(part2())
