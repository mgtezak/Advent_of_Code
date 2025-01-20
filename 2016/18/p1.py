def part1(puzzle_input, is_example_input=False):
    m = 10 if is_example_input else 40
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
