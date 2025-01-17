def part2(puzzle_input):
    grid = [[int(n) for n in line] for line in puzzle_input.split('\n')]
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

    return max(scenic_score.values())
