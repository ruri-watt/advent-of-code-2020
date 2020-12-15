import itertools
from typing import List, Tuple

import numpy as np


def part1():
    with open('room.txt') as f:
        state = np.array([[ord(c) for c in line[:-1]] for line in f])
    coords = np.empty(state.shape, dtype=object)
    coords[:] = [[(x, y) for y in range(state.shape[1])] for x in range(state.shape[0])]

    def get_state(p: Tuple[int, int]):
        if 0 <= p[0] < state.shape[0] and 0 <= p[1] < state.shape[1]:
            return state[p]
        return None

    def get_neighbour_coords(p: Tuple[int, int]):
        directions = [(dx, dy) for dy in range(-1, 2) for dx in range(-1, 2) if (dx, dy) != (0, 0)]
        potential_neighbour_coords = [(p[0] + d[0], p[1] + d[1]) for d in directions]
        return [n for n in potential_neighbour_coords if get_state(n)]

    arr_get_neighbour_coords = np.frompyfunc(get_neighbour_coords, 1, 1)
    neighbour_coords = arr_get_neighbour_coords(coords)

    def states(points: List[Tuple[int, int]]):
        return [state[p] for p in points]

    arr_states = np.frompyfunc(states, 1, 1)
    neighbour_values = arr_states(neighbour_coords)

    def state_transition(p: Tuple[int, int]):
        current_state = state[p]
        nr_occupied_neighbours = len([v for v in neighbour_values[p] if v == ord('#')])
        next_state = current_state
        if current_state == ord('L') and nr_occupied_neighbours == 0:
            next_state = ord('#')
        if current_state == ord('#') and nr_occupied_neighbours >= 4:
            next_state = ord('L')
        return next_state

    arr_state_transition = np.frompyfunc(state_transition, 1, 1)

    next_state = arr_state_transition(coords)
    while np.any(next_state != state):
        state = next_state
        neighbour_values = arr_states(neighbour_coords)
        next_state = arr_state_transition(coords)
    return np.count_nonzero(state == ord('#'))


def part2():
    with open('room.txt') as f:
        state = np.array([[ord(c) for c in line[:-1]] for line in f])
    coords = np.empty(state.shape, dtype=object)
    coords[:] = [[(x, y) for y in range(state.shape[1])] for x in range(state.shape[0])]

    def get_state(p: Tuple[int, int]):
        if 0 <= p[0] < state.shape[0] and 0 <= p[1] < state.shape[1]:
            return state[p]
        return None

    def neighbour_coord(p: Tuple[int, int], d: Tuple[int, int]):
        line_of_sight = ((p[0] + (c * d[0]), p[1] + (c * d[1])) for c in itertools.count(1))
        coord = next(
            p for p in line_of_sight if get_state(p) == ord('L') or get_state(p) == ord('#') or get_state(p) is None)
        if get_state(coord):
            return coord
        return None

    def get_neighbour_coords(p: Tuple[int, int]):
        directions = [(dx, dy) for dy in range(-1, 2) for dx in range(-1, 2) if (dx, dy) != (0, 0)]
        return [neighbour_coord(p, d) for d in directions if neighbour_coord(p, d)]

    arr_get_neighbour_coords = np.frompyfunc(get_neighbour_coords, 1, 1)
    neighbour_coords = arr_get_neighbour_coords(coords)

    def states(points: List[Tuple[int, int]]):
        return [state[p] for p in points]

    arr_states = np.frompyfunc(states, 1, 1)
    neighbour_values = arr_states(neighbour_coords)

    def state_transition(p: Tuple[int, int]):
        current_state = state[p]
        nr_occupied_neighbours = len([v for v in neighbour_values[p] if v == ord('#')])
        next_state = current_state
        if current_state == ord('L') and nr_occupied_neighbours == 0:
            next_state = ord('#')
        if current_state == ord('#') and nr_occupied_neighbours >= 5:
            next_state = ord('L')
        return next_state

    arr_state_transition = np.frompyfunc(state_transition, 1, 1)

    next_state = arr_state_transition(coords)
    while np.any(next_state != state):
        state = next_state
        neighbour_values = arr_states(neighbour_coords)
        next_state = arr_state_transition(coords)
    return np.count_nonzero(state == ord('#'))


if __name__ == '__main__':
    print(part1())
    print(part2())
