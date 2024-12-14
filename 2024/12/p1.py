def part1(puzzle_input):
    grid = puzzle_input.split()
    m = len(grid)
    n = len(grid[0])

    def find_region(i, j):
        plant = grid[i][j]
        visited = set()
        fence = 0
        queue = [(i, j)] 
        while queue:
            i, j = queue.pop()
            if (i, j) in visited:
                continue
            if i not in range(m) or j not in range(n) or grid[i][j] != plant:
                fence += 1
                continue
            visited.add((i, j))
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if (i+x, j+y) not in visited:
                    queue.append((i+x, j+y))
                    
        return visited, len(visited) * fence
            
    total = 0
    visited = set()
    for i in range(m):
        for j in range(n):
            if (i, j) not in visited:
                region, cost = find_region(i, j)
                visited |= region
                total += cost

    return total