from typing import TextIO, Tuple

import numpy as np


class PisteMap:
    def __init__(self, file: TextIO):
        self.matrix = np.array([[c for c in line if c != '\n'] for line in file])
        self.width_repeated = len(self.matrix[0])

    def is_tree(self, p: Tuple[int, int]):
        return self.matrix[int(p[1])][int(p[0]) % self.width_repeated] == '#'

    def is_bottom(self, p: Tuple[int, int]):
        return p[1] >= len(self.matrix)

    def nr_trees(self, slope: Tuple[int, int]):
        nr_trees = 0
        pos = slope
        while not self.is_bottom(pos):
            if self.is_tree(pos):
                nr_trees += 1
            pos = np.add(pos, slope)
        return nr_trees


def part1():
    with open('piste-map.txt') as f:
        piste_map = PisteMap(f)
    return piste_map.nr_trees((3, 1))


def part2():
    with open('piste-map.txt') as f:
        piste_map = PisteMap(f)
    tree_counts = [piste_map.nr_trees(slope) for slope in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))]
    return np.prod(tree_counts)


if __name__ == '__main__':
    print(part1())
    print(part2())
