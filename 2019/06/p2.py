from collections import defaultdict

def part2(puzzle_input):
    lines = [o.split(')') for o in puzzle_input.split('\n')]
    orbits = defaultdict(list)
    for x, y in lines:
        orbits[y].append(x)

    def get_orbits(y):
        if orbits[y] == ['COM']:
            return ['COM']
        return orbits[y] + [get_orbits(x) for x in orbits[y]][0]

    santa = get_orbits('SAN')
    me = get_orbits('YOU')
    return len([x for x in santa + me if not (x in santa and x in me)])