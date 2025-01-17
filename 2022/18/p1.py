import re


def part1(puzzle_input):
    lava_cubes = []
    regex = r'(\d+),(\d+),(\d+)'
    for xyz in re.findall(regex, puzzle_input):
        lava_cubes.append(tuple(map(int, xyz)))

    adjacent = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    return sum((x+a, y+b, z+c) not in lava_cubes for x, y, z in lava_cubes for a, b, c in adjacent)
