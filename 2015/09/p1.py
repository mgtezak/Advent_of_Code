from itertools import permutations


def part1(puzzle_input):
    lines = [line.split() for line in puzzle_input.split('\n')]
    locs = {line[0] for line in lines} | {lines[-1][2]}
    perms = list(permutations(locs))
    distances = {}
    for p in perms:
        total_distance = 0
        for i in range(len(locs)-1):
            start = p[i]
            stop = p[i+1]
            dist = [int(line[-1]) for line in lines if start in line and stop in line][0]
            total_distance += dist

        distances[p] = total_distance

    return min(distances.values())
