import re


def part1(puzzle_input):
    regex = r'(\d+),(\d+) -> (\d+),(\d+)'
    lines = [tuple(map(int, coords)) for coords in re.findall(regex, puzzle_input)]
    horizontal = [(x1, y1, x2, y2) for x1, y1, x2, y2 in lines if x1 == x2 or y1 == y2]
    covered = dict()
    for x1, y1, x2, y2 in horizontal:
        for x in range(min(x1, x2), max(x1, x2)+1):
            for y in range(min(y1, y2), max(y1, y2)+1):
                if not covered.get((x, y)):
                    covered[(x, y)] = 0
                covered[(x, y)] += 1
    return len([(x, y) for x, y in covered if covered[(x, y)] > 1])
