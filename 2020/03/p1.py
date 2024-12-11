def part1(puzzle_input):
    slope = puzzle_input.split('\n')
    tree_count = 0
    j = 0
    l = len(slope[0])
    for row in slope:
        if row[j] == '#':
            tree_count += 1
        j = (j + 3) % l
    return tree_count