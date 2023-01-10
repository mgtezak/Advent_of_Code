with open('Advent_of_Code/2022/puzzle_input/08.txt') as input:
    grid = [[int(n) for n in line] for line in input.read().split('\n')]

# part 1:
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

part1 = len(visible)

# part 2: 
scenic_score = {}
for y in range(len(grid)):
    for x in range(len(grid[0])):

        down = up = right = left = 0
        treehouse = grid[y][x]
        
        # look right
        for col in range(x+1, len(grid[0])):
            right += 1
            if grid[y][col] >= treehouse:
                break

        # look left
        for col in range(x-1, -1, -1):
            left += 1
            if grid[y][col] >= treehouse:
                break

        # look down
        for row in range(y+1, len(grid)):
            down += 1
            if grid[row][x] >= treehouse:
                break

        # look up
        for row in range(y-1, -1, -1):
            up += 1
            if grid[row][x] >= treehouse:
                break
                    
        scenic_score[(x, y)] = down * up * right * left

part2 = max(scenic_score.values())

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')