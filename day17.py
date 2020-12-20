import numpy as np


class InfiniteCube:
    def __init__(self, initial_state):
        self.state = initial_state
        self.state = self.init_next_state()

    def init_next_state(self):
        next_state = np.zeros(np.add(self.state.shape, 2), dtype=bool)
        next_state[1:-1, 1:-1, 1:-1] = self.state
        return next_state

    def advance(self):
        next_state = self.init_next_state()
        self.state = np.copy(next_state)
        for z in range(1, self.state.shape[0] - 1):
            for y in range(1, self.state.shape[1] - 1):
                for x in range(1, self.state.shape[2] - 1):
                    sub_cube = self.state[z - 1:z + 2, y - 1:y + 2, x - 1:x + 2]
                    nr_active = np.count_nonzero(sub_cube)
                    if self.state[z, y, x]:
                        next_state[z, y, x] = 3 <= nr_active <= 4
                    else:
                        next_state[z, y, x] = nr_active == 3
        self.state = next_state


class InfiniteHypercube:
    def __init__(self, initial_state):
        self.state = initial_state
        self.state = self.init_next_state()

    def init_next_state(self):
        next_state = np.zeros(np.add(self.state.shape, 2), dtype=bool)
        next_state[1:-1, 1:-1, 1:-1, 1:-1] = self.state
        return next_state

    def advance(self):
        next_state = self.init_next_state()
        self.state = np.copy(next_state)
        for w in range(1, self.state.shape[0] - 1):
            for z in range(1, self.state.shape[1] - 1):
                for y in range(1, self.state.shape[2] - 1):
                    for x in range(1, self.state.shape[3] - 1):
                        sub_cube = self.state[w - 1:w + 2, z - 1:z + 2, y - 1:y + 2, x - 1:x + 2]
                        nr_active = np.count_nonzero(sub_cube)
                        if self.state[w, z, y, x]:
                            next_state[w, z, y, x] = 3 <= nr_active <= 4
                        else:
                            next_state[w, z, y, x] = nr_active == 3
        self.state = next_state


def part1():
    with open('conway-cubes.txt') as f:
        state = np.array([[[c == '#' for c in line[:-1]] for line in f]])
    cube = InfiniteCube(state)
    for _ in range(6):
        cube.advance()
    return np.count_nonzero(cube.state)


def part2():
    with open('conway-cubes.txt') as f:
        state = np.array([[[[c == '#' for c in line[:-1]] for line in f]]])
    cube = InfiniteHypercube(state)
    for _ in range(6):
        cube.advance()
    return np.count_nonzero(cube.state)


if __name__ == '__main__':
    print(part1())
    print(part2())
