import math


class Leg:
    def __init__(self, instruction: str, distance: int):
        self.instruction = instruction.lower()
        self.distance = distance


class Boat:
    def __init__(self):
        self.direction = complex(1, 0)
        self.position = [0, 0]

    def apply(self, leg: Leg):
        getattr(self, leg.instruction)(leg.distance)

    def n(self, distance: int):
        self.position[1] += distance

    def s(self, distance: int):
        self.position[1] -= distance

    def e(self, distance: int):
        self.position[0] += distance

    def w(self, distance: int):
        self.position[0] -= distance

    def l(self, angle: int):
        rot = complex(0, 1) ** (angle // 90)
        self.direction *= rot

    def r(self, angle: int):
        rot = complex(0, -1) ** (angle // 90)
        self.direction *= rot

    def f(self, distance: int):
        self.position[0] += distance * int(self.direction.real)
        self.position[1] += distance * int(self.direction.imag)


class Navigator:
    def __init__(self):
        self.boat_position = complex(0, 0)
        self.waypoint_position = complex(10, 1)

    def apply(self, leg: Leg):
        getattr(self, leg.instruction)(leg.distance)

    def n(self, distance: int):
        self.waypoint_position += complex(0, distance)

    def s(self, distance: int):
        self.waypoint_position -= complex(0, distance)

    def e(self, distance: int):
        self.waypoint_position += distance

    def w(self, distance: int):
        self.waypoint_position -= distance

    def l(self, angle: int):
        rot = complex(0, 1) ** (angle // 90)
        self.waypoint_position *= rot

    def r(self, angle: int):
        rot = complex(0, -1) ** (angle // 90)
        self.waypoint_position *= rot

    def f(self, multiple: int):
        self.boat_position += multiple * self.waypoint_position


def part1():
    with open('boat-navigation.txt') as f:
        legs = [Leg(line[0], int(line[1:])) for line in f]
    boat = Boat()
    for leg in legs:
        boat.apply(leg)
    manhatten_distance = abs(boat.position[0]) + abs(boat.position[1])
    return manhatten_distance

def part2():
    with open('boat-navigation.txt') as f:
        legs = [Leg(line[0], int(line[1:])) for line in f]
    navigator = Navigator()
    for leg in legs:
        navigator.apply(leg)
    manhatten_distance = abs(navigator.boat_position.real) + abs(navigator.boat_position.imag)
    return manhatten_distance


if __name__ == '__main__':
    print(part1())
    print(part2())
