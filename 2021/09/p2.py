import math

def part2(puzzle_input):
    grid = [[int(n) for n in row] for row in puzzle_input.split('\n')]
    x_range = range(len(grid[0]))
    y_range = range(len(grid))

    def get_neighbors(x, y):
        adj = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i, j in adj:
            if x+i in x_range and y+j in y_range:
                yield x+i, y+j

    def add_basin():
        size = 0
        queue = [unvisited.pop()]
        while queue:
            x, y = queue.pop()
            if grid[y][x] == 9:
                continue
            size += 1
            for i, j in get_neighbors(x, y):
                if (i, j) in unvisited:
                    unvisited.remove((i, j))
                    queue.append((i, j))
        basins.append(size) 

    unvisited = [(x, y) for x in x_range for y in y_range]  
    basins = []
    while unvisited:
        add_basin()

    return math.prod(sorted(basins)[-3:])