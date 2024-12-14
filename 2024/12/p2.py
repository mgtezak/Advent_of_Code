def part2(puzzle_input):
    grid = puzzle_input.split()
    m = len(grid)
    n = len(grid[0])

    def get_corners(i, j):
        NW, W, SW, N, S, NE, E, SE = [
            is_same(i+x, j+y, grid[i][j])
            for x in range(-1, 2) 
            for y in range(-1, 2) 
            if x or y
        ]
        return sum([
            N and W and not NW, 
            N and E and not NE, 
            S and W and not SW, 
            S and E and not SE, 
            not (N or W),
            not (N or E),
            not (S or W),
            not (S or E)
        ])
    
    def is_same(i, j, plant):
        return (
            i in range(m) and 
            j in range(n) and 
            grid[i][j] == plant
        )
    
    def find_region(i, j):
        plant = grid[i][j]
        region = set()
        queue = set([(i, j)])
        while queue:
            i, j = queue.pop()
            region.add((i, j))
            for x, y in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]:
                if (x in range(m) and 
                    y in range(n) and 
                    grid[x][y] == plant and
                    (x, y) not in region and
                    (x, y) not in queue
                ):
                    queue.add((x, y))
    
        corners = sum(get_corners(x, y) for x, y in region)
        return region, corners * len(region)

    total = 0
    visited = set()
    for i in range(m):
        for j in range(n):
            if (i, j) not in visited:
                region, cost = find_region(i, j)
                total += cost
                visited |= region

    return total
