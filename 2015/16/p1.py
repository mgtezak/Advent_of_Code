import re


def part1(puzzle_input):

    regex = r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)'
    sues = {int(i): {a: int(b), c: int(d), e: int(f)} for i, a, b, c, d, e, f in re.findall(regex, puzzle_input)}
    evidence = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }

    for sue, items in sues.items():
        if all(count == evidence[i] for i, count in items.items()):
            return sue
