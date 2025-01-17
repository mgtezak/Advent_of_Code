def part1(puzzle_input):
    grid = puzzle_input.splitlines()
    n, m = len(grid), len(grid[0])
    r, c = 0, grid[0].find('|')
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    d = 0
    message = ''

    def check(r, c):
        return (
            r in range(n) and 
            c in range(m) and
            grid[r][c] != ' '
        )

    while True:
        r += directions[d][0]
        c += directions[d][1]
        if grid[r][c] == ' ':
            break
        if grid[r][c] == '+':
            d1 = (d - 1) % 4
            d2 = (d + 1) % 4
            x = r + directions[d1][0]
            y = c + directions[d1][1]
            d = d1 if check(x, y) else d2
        elif grid[r][c].isalpha():
            message += grid[r][c]

    return message
