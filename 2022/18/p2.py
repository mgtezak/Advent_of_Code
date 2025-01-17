import re


def part2(puzzle_input):
    lava_cubes = []
    regex = r'(\d+),(\d+),(\d+)'
    for xyz in re.findall(regex, puzzle_input):
        lava_cubes.append(tuple(map(int, xyz)))

    adjacent = [
        (1, 0, 0), 
        (-1, 0, 0), 
        (0, 1, 0), 
        (0, -1, 0), 
        (0, 0, 1), 
        (0, 0, -1)
    ]

    # expand dimensions by one on each side:
    dim = range(-1, 21)

    n_visible_sides = 0
    queue = [(0, 0, 0)]
    visited = set()

    while queue:
        x, y, z = queue.pop()
        visited.add((x, y, z))
        for a, b, c in adjacent:
            q, r, s = x+a, y+b, z+c
            if (
                q in dim and 
                r in dim and 
                s in dim and 
                not ((q, r, s) in visited or (q, r, s) in queue)
            ):
                if (q, r, s) in lava_cubes:
                    n_visible_sides += 1
                else:
                    queue.append((q, r, s))

    return n_visible_sides
