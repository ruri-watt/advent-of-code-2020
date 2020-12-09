import re


class Bag:
    def __init__(self, line: str):
        self.color, *contents = re.split(r' bags contain | bag, | bags, ', line)
        contents[-1] = contents[-1][:contents[-1].index(' bag')]
        try:
            self.contents = [(int(s.split(' ', 1)[0]), s.split(' ', 1)[1]) for s in contents]
        except ValueError:
            self.contents = []


def part1():
    parent_colors = {}
    with open('bag-rules.txt') as f:
        for line in f:
            bag = Bag(line)
            for child in bag.contents:
                try:
                    parent_colors[child[1]].append(bag.color)
                except KeyError:
                    parent_colors[child[1]] = [bag.color]
    ancestors = set()
    bags = {'shiny gold'}
    while bags:
        parents = {p for bag in bags for p in parent_colors.get(bag, [])}
        ancestors.update(parents)
        bags = parents
    return len(ancestors)


def part2():
    bag_contents = {}
    with open('bag-rules.txt') as f:
        for line in f:
            bag = Bag(line)
            bag_contents[bag.color] = bag.contents

    def nr_bags_in(bag: str):
        if not bag_contents[bag]:
            return 0
        contents = bag_contents[bag]
        return sum([bag[0] + bag[0] * nr_bags_in(bag[1]) for bag in contents])

    return nr_bags_in('shiny gold')


if __name__ == '__main__':
    print(part1())
    print(part2())
