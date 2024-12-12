import heapq

def part2(puzzle_input):
    grid = [[int(i) for i in row] for row in puzzle_input.split()]
    n = len(grid)

    # Expand width
    for r in range(n):
        for s in range(1, 5):
            grid[r].extend([(i - 1 + s) % 9 + 1 for i in grid[r][:n]])

    # Expand length
    for s in range(1, 5):
        for r in range(n):
            grid.append([(i - 1 + s) % 9 + 1 for i in grid[r]])

    upper = len(grid) - 1
    visited = set()
    heap = [(0, 0, 0)]
    while heap:
        total, x, y = heapq.heappop(heap)
        if (x, y) in visited:
            continue
        if x == y == upper:
            break
        if x > 0:
            heapq.heappush(heap, (total + grid[x-1][y], x-1, y))
        if x < upper:
            heapq.heappush(heap, (total + grid[x+1][y], x+1, y))
        if y > 0:
            heapq.heappush(heap, (total + grid[x][y-1], x, y-1))
        if y < upper:
            heapq.heappush(heap, (total + grid[x][y+1], x, y+1))
        visited.add((x, y))

    return total