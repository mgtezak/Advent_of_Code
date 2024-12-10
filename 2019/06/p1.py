from collections import defaultdict

def part1(puzzle_input):
    lines = [o.split(')') for o in puzzle_input.split('\n')]
    orbits = defaultdict(list)
    for x, y in lines:
        orbits[y].append(x)

    def get_orbits(y):
        if orbits[y] == ['COM']:
            return ['COM']
        return orbits[y] + [get_orbits(x) for x in orbits[y]][0]

    return sum(len(get_orbits(y)) for y in orbits)