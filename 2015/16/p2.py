import re


def part2(puzzle_input):

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
        for i, count in items.items():
            if i in ('cats', 'trees'):
                if count <= evidence[i]:
                    break
            elif i in ('pomeranians', 'goldfish'):
                if count >= evidence[i]:
                    break
            elif count != evidence[i]:
                break
        else:
            return sue
