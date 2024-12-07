import math


def part2(puzzle_input):
    total_ribbon = 0
    for line in puzzle_input.split('\n'):
        edges = [int(edge) for edge in line.split('x')]
        total_ribbon += math.prod(edges)
        edges.remove(max(edges))
        total_ribbon += sum(edges * 2)
    return total_ribbon
