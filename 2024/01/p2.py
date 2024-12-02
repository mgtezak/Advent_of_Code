from collections import defaultdict

def part2(puzzle_input):
    first = defaultdict(int)
    second = defaultdict(int)
    for line in puzzle_input.split('\n'):
        a, b = map(int, line.split())
        first[a] += 1
        second[b] += 1

    similarity = 0
    for num, count in first.items():
        similarity += num * count * second[num]

    return similarity
