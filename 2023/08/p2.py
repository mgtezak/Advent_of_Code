import re
from itertools import cycle
import math


def part2(puzzle_input):
    directions, connections = puzzle_input.split('\n\n')
    directions = [0 if d == 'L' else 1 for d in directions]
    graph = {}
    regex = r'(\w{3}) = \((\w{3}), (\w{3})\)'
    for node, left, right in re.findall(regex, connections):
        graph[node] = [left, right]

    starting_nodes = [node for node in graph if node[2] == 'A']
    cycles = []
    for node in starting_nodes:
        for steps, d in enumerate(cycle(directions), start=1):
            node = graph[node][d]
            if node[2] == 'Z':
                cycles.append(steps)
                break

    return math.lcm(*cycles)
