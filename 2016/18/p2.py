def part2(puzzle_input):
    m = 400_000
    n = len(puzzle_input)
    traps = {'^^.', '.^^', '^..', '..^'}
    row = puzzle_input
    safe = row.count('.')
    for _ in range(m-1):
        prev = '.' + row + '.'
        row = ''
        for i in range(n):
            row += '^' if prev[i:i+3] in traps else '.'

        safe += row.count('.')

    return safe
