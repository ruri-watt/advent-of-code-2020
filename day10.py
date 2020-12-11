import numpy as np


def part1():
    with open('joltage-adapters.txt') as f:
        adapters = [int(line) for line in f]
    ratings = sorted(adapters + [0, max(adapters) + 3])
    ratings = np.array(ratings)
    diffs = ratings[1:] - ratings[:-1]
    return np.count_nonzero(diffs == 1) * np.count_nonzero(diffs == 3)


def part2():
    with open('joltage-adapters.txt') as f:
        adapters = [int(line) for line in f]
    ratings = sorted(adapters + [0, max(adapters) + 3])
    neighbours = {rating: {r for r in ratings if 0 < r - rating <= 3} for rating in ratings}
    destination = ratings[-1]
    nr_paths = {destination: 1}
    for n in reversed(ratings[:-1]):
        nr_paths[n] = sum([nr_paths[i] for i in neighbours[n]])
    return nr_paths[0]


if __name__ == '__main__':
    print(part1())
    print(part2())
