import itertools
import re


class Computer:
    def __init__(self):
        self.memory = dict()
        self.or_bitmask = 0
        self.and_bitmask_inverse = 0
        self.memory_address_masks = []

    def set_bitmask(self, bitmask: str):
        self.or_bitmask = int(bitmask.replace('X', '0'), base=2)
        self.and_bitmask_inverse = int(bitmask.replace('1', 'X').replace('0', '1').replace('X', '0'), base=2)

    def set_memory(self, pos: int, val: int):
        self.memory[pos] = (val | self.or_bitmask) & ~self.and_bitmask_inverse

    def set_memory2(self, pos: int, val: int):
        for or_bitmask, and_bitmask_inverse in self.memory_address_masks:
            self.memory[(pos | or_bitmask) & ~and_bitmask_inverse] = val

    def set_memory_mask(self, memory_mask):
        floating_indices = [i for i, c in enumerate(memory_mask) if c == 'X']
        floating_value_choices = itertools.product('01', repeat=len(floating_indices))
        self.memory_address_masks = []
        for choice in floating_value_choices:
            forced_bits = list(memory_mask.replace('0', '-'))
            for index, bit_value in zip(floating_indices, choice):
                forced_bits[index] = bit_value
            forced_bits = ''.join(forced_bits)
            or_bitmask = int(forced_bits.replace('-', '0'), base=2)
            and_bitmask_inverse = int(forced_bits.replace('1', '-').replace('0', '1').replace('-', '0'), base=2)
            self.memory_address_masks.append((or_bitmask, and_bitmask_inverse))


def part1():
    computer = Computer()
    with open('docking-data.txt') as f:
        for line in f:
            if line.startswith('mask'):
                computer.set_bitmask(re.search(r'([X01]+)', line)[0])
            elif line.startswith('mem'):
                pos, val = map(int, re.findall(r'([0-9]+)', line))
                computer.set_memory(pos, val)
    return sum(computer.memory.values())

def part2():
    computer = Computer()
    with open('docking-data.txt') as f:
        for line in f:
            if line.startswith('mask'):
                computer.set_memory_mask(re.search(r'([X01]+)', line)[0])
            elif line.startswith('mem'):
                pos, val = map(int, re.findall(r'([0-9]+)', line))
                computer.set_memory2(pos, val)
    return sum(computer.memory.values())



if __name__ == '__main__':
    print(part1())
    print(part2())
