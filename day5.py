def seat_id(seat):
    return 8 * seat[0] + seat[1]


def seat_pos(line):
    row_range = [0, 128]
    column_range = [0, 8]
    for char in line:
        if char == 'F':
            row_range[1] -= (row_range[1] - row_range[0]) // 2
        elif char == 'B':
            row_range[0] += (row_range[1] - row_range[0]) // 2
        elif char == 'L':
            column_range[1] -= (column_range[1] - column_range[0]) // 2
        elif char == 'R':
            column_range[0] += (column_range[1] - column_range[0]) // 2
    assert row_range[0] == row_range[1] - 1
    assert column_range[0] == column_range[1] - 1
    return row_range[0], column_range[0]


def part1():
    with open('seats.txt') as f:
        seat_ids = []
        for line in f:
            seat_ids.append(seat_id(seat_pos(line)))
    return max(seat_ids)


def part2():
    all_seats = {(row, col) for row in range(128) for col in range(8)}
    taken_seats = set()
    with open('seats.txt') as f:
        for line in f:
            taken_seats.add(seat_pos(line))
    available_seat_ids = {seat_id(seat) for seat in (all_seats - taken_seats)}
    possible_solutions = [sid for sid in available_seat_ids if
                          sid + 1 not in available_seat_ids and sid - 1 not in available_seat_ids]
    assert len(possible_solutions) == 1
    return possible_solutions[0]


if __name__ == '__main__':
    print(part1())
    print(part2())
