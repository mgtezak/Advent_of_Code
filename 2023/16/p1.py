def part1(puzzle_input):
    grid = [list(r) for r in puzzle_input.split('\n')]
    m, n = len(grid), len(grid[0])
    visited = set()
    energized = set()
    queue = set([(0, 0, 'right')])   
    while queue:
        x, y, direction = queue.pop()
        energized.add((x, y))
        tile = grid[x][y]

        if y < n-1 and (x, y+1, 'right') not in visited and (
                (direction == 'right' and tile in '.-') or 
                (direction == 'up' and tile in '/-') or
                (direction == 'down' and tile in '\\-')):
            queue.add((x, y+1, 'right'))
            visited.add((x, y+1, 'right'))

        if x > 0 and (x-1, y, 'up') not in visited and (
                (direction == 'up' and tile in '.|') or 
                (direction == 'right' and tile in '/|') or
                (direction == 'left' and tile in '\\|')):
            queue.add((x-1, y, 'up'))
            visited.add((x-1, y, 'up'))

        if y > 0 and (x, y-1, 'left') not in visited and (
                (direction == 'left' and tile in '.-') or 
                (direction == 'up' and tile in '\\-') or
                (direction == 'down' and tile in '/-')):
            queue.add((x, y-1, 'left'))
            visited.add((x, y-1, 'left'))

        if x < m-1 and (x+1, y, 'down') not in visited and (
                (direction == 'down' and tile in '.|') or 
                (direction == 'right' and tile in '\\|') or
                (direction == 'left' and tile in '/|')):
            queue.add((x+1, y, 'down'))     
            visited.add((x+1, y, 'down'))

    return len(energized)
