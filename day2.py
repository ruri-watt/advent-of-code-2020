class Password:
    def __init__(self, occurrences_def: str, letter_def: str, password: str):
        self.min = int(occurrences_def.split('-')[0])
        self.max = int(occurrences_def.split('-')[1])
        self.letter = letter_def[0]
        self.password = password

    def is_valid(self):
        return self.min <= self.password.count(self.letter) <= self.max

    def is_valid2(self):
        i = self.min - 1
        j = self.max - 1
        return (self.password[i] == self.letter) ^ (self.password[j] == self.letter)


def part1():
    with open('passwords.txt') as f:
        passwords = [Password(*line.split(' ')) for line in f]
    valid_passwords = [p for p in passwords if p.is_valid()]
    return len(valid_passwords)


def part2():
    with open('passwords.txt') as f:
        passwords = [Password(*line.split(' ')) for line in f]
    valid_passwords = [p for p in passwords if p.is_valid2()]
    return len(valid_passwords)


if __name__ == '__main__':
    print(part1())
    print(part2())
