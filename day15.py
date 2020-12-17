starting_numbers = [7, 12, 1, 0, 16, 2]


def add_turn(numbers, greatest_index):
    try:
        i = greatest_index[numbers[-1]]
        numbers.append(len(numbers) - 1 - i)
    except KeyError:
        numbers.append(0)
    greatest_index[numbers[-2]] = len(numbers) - 2


def part1(stop_at=2020):
    numbers = starting_numbers[:]
    greatest_index = {n: i for i, n in enumerate(numbers[:-1])}
    while len(numbers) < stop_at:
        add_turn(numbers, greatest_index)
    return numbers[-1]


def part2():
    return part1(30000000)


if __name__ == '__main__':
    print(part1())
    print(part2())
