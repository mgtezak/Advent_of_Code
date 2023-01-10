with open('Advent_of_Code/2022/puzzle_input/12.txt') as input:
    lines = [line for line in input.read().split('\n')]


grid = [[] for _ in lines]
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == 'S':                        # elevation at S = a
            x_start, y_start, char = x, y, 'a'
        elif char == 'E':                      # elevation at E = z 
            x_end, y_end, char = x, y, 'z'
        grid[y].append(ord(char) - 97)         # turn letters (a-z) into numbers (0-25)


x_range, y_range = range(len(grid[0])), range(len(grid))

def validate_move(x: int, y: int, elevation: int) -> bool:
    '''returns True if the coordinates are inside the grid and the climb is not too steep'''
    return (x in x_range) and (y in y_range) and (grid[y][x] < elevation + 2)


def get_shortest_distance(start: tuple=(x_start, y_start), end: tuple=(x_end, y_end)) -> int:
    '''Breadth-first-search algorithm that finds the shortest path and returns number of steps if path exists'''
    
    steps = elevation = 0
    visited = {start: (steps, elevation)}
    queue = [start]

    while queue:
        x, y = queue.pop(0)
        steps, elevation = visited[(x, y)]
        
        if (x, y) ==  end:
            return steps

        moves = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        possible_moves = [(x, y) for x, y in moves if validate_move(x, y, elevation)]

        for x, y in possible_moves:
            if (x, y) not in visited:
                visited[(x, y)] = (steps + 1, grid[y][x])
                queue.append((x, y))


possible_starts = [(x, y) for y, row in enumerate(grid) for x, elevation in enumerate(row) if elevation == 0]
possible_steps = [get_shortest_distance(coords) for coords in possible_starts]
min_steps = min([steps for steps in possible_steps if steps])


print(f'Part 1: {get_shortest_distance((x_start, y_start))}')
print(f'Part 2: {min_steps}')