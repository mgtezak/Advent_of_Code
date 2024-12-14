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
            for x, y in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]:
                if (x, y) not in visited:
                    queue.append((x, y))
                    
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