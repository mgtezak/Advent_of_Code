import re
from itertools import cycle


def part1(puzzle_input):
    directions, connections = puzzle_input.split('\n\n')
    directions = cycle(0 if d == 'L' else 1 for d in directions)
    graph = {}
    regex = r'(\w{3}) = \((\w{3}), (\w{3})\)'
    for node, left, right in re.findall(regex, connections):
        graph[node] = [left, right]

    node = 'AAA'
    for steps, d in enumerate(directions, start=1):
        node = graph[node][d]
        if node == 'ZZZ':
            break

    return steps
