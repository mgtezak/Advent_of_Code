def part1(puzzle_input):
    first = []
    second = []
    for line in puzzle_input.split('\n'):
        a, b = map(int, line.split())
        first.append(a)
        second.append(b)

    distance = 0
    for a, b in zip(sorted(first), sorted(second)):
        distance += abs(a - b)

    return distance
