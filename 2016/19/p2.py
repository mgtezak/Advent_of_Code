def part2(puzzle_input):
    n = int(puzzle_input)
    i = 1
    while 3*i < n:
        i *= 3

    if n <= 2*i:
        return n - i
    return 2*n - 3*i
