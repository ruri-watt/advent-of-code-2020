from typing import Tuple


class GameConsole:
    def __init__(self, boot_code):
        self.boot_code = boot_code
        self.accumulator = 0
        self.op_ptr = 0
        self.ops_done = set()

    def step(self, op_override=None):
        op, arg = self.boot_code[self.op_ptr]
        if op_override:
            op = op_override
        self.ops_done.add(self.op_ptr)
        self.op_ptr = getattr(self, op)(arg)

    def reset(self):
        self.accumulator = 0
        self.op_ptr = 0
        self.ops_done = set()

    def acc(self, val):
        self.accumulator += val
        return self.op_ptr + 1

    def jmp(self, val):
        return self.op_ptr + val

    def nop(self, _):
        return self.op_ptr + 1

    def alt_op(self):
        op, _ = self.boot_code[self.op_ptr]
        alt = None
        if op == 'jmp':
            alt = 'nop'
        elif op == 'nop':
            alt = 'jmp'
        return alt

    def loop_detected(self):
        return self.op_ptr in self.ops_done

    def is_booted(self):
        return self.op_ptr >= len(self.boot_code)


def instruction(line) -> Tuple[str, int]:
    split = line.split(' ')
    return split[0], int(split[1])


def part1():
    with open('boot-code.txt') as f:
        game_console = GameConsole([instruction(l) for l in f])
    while not game_console.loop_detected():
        game_console.step()
    return game_console.accumulator


def part2():
    with open('boot-code.txt') as f:
        game_console = GameConsole([instruction(l) for l in f])
    alt_ops_tested = set()

    while not game_console.is_booted():
        game_console.reset()
        op_modified = False
        while not game_console.loop_detected() and not game_console.is_booted():
            if not op_modified and game_console.alt_op() and game_console.op_ptr not in alt_ops_tested:
                op_modified = True
                alt_ops_tested.add(game_console.op_ptr)
                game_console.step(game_console.alt_op())
            else:
                game_console.step()
    return game_console.accumulator


if __name__ == '__main__':
    print(part1())
    print(part2())
