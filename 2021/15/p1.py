import heapq

def part1(puzzle_input):
    grid = [[int(i) for i in row] for row in puzzle_input.split()]
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