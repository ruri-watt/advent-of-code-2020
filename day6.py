def part1():
    with open('passport-control-answers.txt') as f:
        answer_sets = [set(char for char in group.replace('\n', '')) for group in f.read().split('\n\n')]
        return sum(len(s) for s in answer_sets)


def part2():
    with open('passport-control-answers.txt') as f:
        groups = [[set(word) for word in group.split('\n')] for group in f.read()[:-1].split('\n\n')]
        intersections = [answer_sets[0].intersection(*answer_sets) for answer_sets in groups]
        return sum(len(s) for s in intersections)


if __name__ == '__main__':
    print(part1())
    print(part2())
