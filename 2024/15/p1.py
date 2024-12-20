def part1(puzzle_input):
    grid, directions = puzzle_input.split('\n\n')
    grid = [list(row) for row in grid.split('\n')]
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '@':
                robot = (i, j)
                grid[i][j] = '.'

    for d in directions[:]:
        i, j = robot
        
        if d == '<':
            k = j-1
            while grid[i][k] == 'O':
                k -= 1
            if grid[i][k] == '.':
                grid[i][k], grid[i][j-1] = grid[i][j-1], grid[i][k]
                robot = (i, j-1)

        elif d == '>':
            k = j+1
            while grid[i][k] == 'O':
                k += 1
            if grid[i][k] == '.':
                grid[i][k], grid[i][j+1] = grid[i][j+1], grid[i][k]
                robot = (i, j+1)

        elif d == '^':
            k = i-1
            while grid[k][j] == 'O':
                k -= 1
            if grid[k][j] == '.':
                grid[k][j], grid[i-1][j] = grid[i-1][j], grid[k][j]
                robot = (i-1, j)

        elif d== 'v':
            k = i+1
            while grid[k][j] == 'O':
                k += 1
            if grid[k][j] == '.':
                grid[k][j], grid[i+1][j] = grid[i+1][j], grid[k][j]
                robot = (i+1, j)

    total = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'O':
                total += 100*i + j

    return total
