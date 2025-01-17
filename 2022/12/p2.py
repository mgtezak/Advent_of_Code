def part2(puzzle_input):
    lines = puzzle_input.split('\n')
    grid = [[] for _ in lines]
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == 'S':                        # elevation at S = a
                char = 'a'
            elif char == 'E':                      # elevation at E = z 
                x_end, y_end, char = x, y, 'z'
            grid[y].append(ord(char) - 97)         # turn letters (a-z) into numbers (0-25)

    x_range, y_range = range(len(grid[0])), range(len(grid))

    def validate_move(x: int, y: int, elevation: int) -> bool:
        '''returns True if the coordinates are inside the grid and the climb is not too steep'''
        return (x in x_range) and (y in y_range) and (grid[y][x] < elevation + 2)

    def get_shortest_distance(x_start, y_start) -> int:
        '''Breadth-first-search algorithm that finds the shortest path and returns number of steps if path exists'''
        
        steps = elevation = 0
        visited = {(x_start, y_start): (steps, elevation)}
        queue = [(x_start, y_start)]

        while queue:
            x, y = queue.pop(0)
            steps, elevation = visited[(x, y)]
            
            if x == x_end and y == y_end:
                break

            moves = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            possible_moves = [(x, y) for x, y in moves if validate_move(x, y, elevation)]

            for x, y in possible_moves:
                if (x, y) not in visited:
                    visited[(x, y)] = (steps + 1, grid[y][x])
                    queue.append((x, y))
            
        return steps if queue else float('inf')

    possible_starts = [(x, y) for y, row in enumerate(grid) for x, elevation in enumerate(row) if elevation == 0]
    return min(get_shortest_distance(*coords) for coords in possible_starts)
