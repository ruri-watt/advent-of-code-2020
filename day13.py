import math


def departs(bus_id, time):
    return time % bus_id == 0


def wait_time(start_time: int, bus_period: int):
    minutes_late = start_time % bus_period
    if minutes_late == 0:
        return 0
    else:
        return bus_period - minutes_late


def part1():
    with open('bus-times.txt') as f:
        earliest_departure_time = int(f.readline())
        bus_ids = [int(bus_id) for bus_id in f.readline()[:-1].split(',') if bus_id != 'x']
    wait_times = [wait_time(earliest_departure_time, bus_id) for bus_id in bus_ids]
    bus, wait = min(zip(bus_ids, wait_times), key=lambda t: t[1])
    return bus * wait


def part2():
    with open('bus-times.txt') as f:
        earliest_departure_time = int(f.readline())
        buses = [(int(bus_id), offset) for offset, bus_id in enumerate(f.readline()[:-1].split(',')) if bus_id != 'x']
    buses.sort(reverse=True)
    slowest_bus_id, slowest_bus_offset = buses[0]
    buses = [(bus_id, offset - slowest_bus_offset) for bus_id, offset in buses]

    t = 0
    dt = slowest_bus_id
    nr_in_phase = 1
    while nr_in_phase < len(buses):
        t += dt
        buses_in_phase = [b for b in buses if departs(b[0], t + b[1])]
        if len(buses_in_phase) > nr_in_phase:
            nr_in_phase = len(buses_in_phase)
            dt = math.lcm(*[b[0] for b in buses_in_phase])
    return t - slowest_bus_offset


if __name__ == '__main__':
    print(part1())
    print(part2())
