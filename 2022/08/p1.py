def part1(puzzle_input):
    grid = [[int(n) for n in line] for line in puzzle_input.split('\n')]
    visible = set()
    for row in range(len(grid)):
        tallest = -1
        for col in range(len(grid[0])):
            if grid[row][col] > tallest:
                visible.add((row, col))
                tallest = grid[row][col]
                
        tallest = -1
        for col in range(len(grid[0])-1, -1, -1):
            if grid[row][col] > tallest:
                visible.add((row, col))
                tallest = grid[row][col]
                
    for col in range(len(grid[0])):
        tallest = -1
        for row in range(len(grid)):
            if grid[row][col] > tallest:
                visible.add((row, col))
                tallest = grid[row][col]
                
        tallest = -1
        for row in range(len(grid)-1, -1, -1):
            if grid[row][col] > tallest:
                visible.add((row, col))
                tallest = grid[row][col]

    return len(visible)
