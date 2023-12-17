from heapq import heappop, heappush

with open('Advent_of_Code/2023/puzzle_input/17.txt', 'r') as f:
    puzzle_input = f.read()


def part1(puzzle_input):
    grid = [[int(d) for d in line] for line in puzzle_input.split('\n')]
    m, n = len(grid), len(grid[0])

    # tuple: (heat-loss, x-coord, y-coord, length-of-current-run, current-direction)
    q = [(0, 0, 0, 0, 'none')] 
    visited = set()
    while q:
        loss, x, y, k, dir = heappop(q)
        if x == m-1 and y == n-1:
            break

        if any((x, y, k_, dir) in visited for k_ in range(1, k+1)):
            continue
    
        visited.add((x, y, k, dir))

        if x > 0 and dir != 'down' and (dir != 'up' or k != 3):
            k_ = 1 if dir != 'up' else 1+k
            heappush(q, (loss + grid[x-1][y], x-1, y, k_, 'up'))

        if x < m-1 and dir != 'up' and (dir != 'down' or k != 3):
            k_ = 1 if dir != 'down' else 1+k
            heappush(q, (loss + grid[x+1][y], x+1, y, k_, 'down'))

        if y > 0 and dir != 'right' and (dir != 'left' or k != 3):
            k_ = 1 if dir != 'left' else 1+k
            heappush(q, (loss + grid[x][y-1], x, y-1, k_, 'left'))

        if y < n-1 and dir != 'left' and (dir != 'right' or k != 3):
            k_ = 1 if dir != 'right' else 1+k
            heappush(q, (loss + grid[x][y+1], x, y+1, k_, 'right'))

    return loss


def part2(puzzle_input):
    grid = [[int(d) for d in line] for line in puzzle_input.split('\n')]
    m, n = len(grid), len(grid[0])

    # tuple: (heat-loss, x-coord, y-coord, length-of-current-run, current-direction)
    q = [(0, 0, 0, 0, 'right'), (0, 0, 0, 0, 'down')] 
    visited = set()
    while q:
        loss, x, y, k, dir = heappop(q)
        if x == m-1 and y == n-1:
            if k < 4:
                continue
            break

        if (x, y, k, dir) in visited:
            continue
    
        visited.add((x, y, k, dir))

        if x > 0 and dir != 'down' and ((dir == 'up' and k < 10) or (dir != 'up' and k >= 4)):
            k_ = 1 if dir != 'up' else 1+k
            heappush(q, (loss + grid[x-1][y], x-1, y, k_, 'up'))

        if x < m-1 and dir != 'up' and ((dir == 'down' and k < 10) or (dir != 'down' and k >= 4)):
            k_ = 1 if dir != 'down' else 1+k
            heappush(q, (loss + grid[x+1][y], x+1, y, k_, 'down'))

        if y > 0 and dir != 'right' and ((dir == 'left' and k < 10) or (dir != 'left' and k >= 4)):
            k_ = 1 if dir != 'left' else 1+k
            heappush(q, (loss + grid[x][y-1], x, y-1, k_, 'left'))

        if y < n-1 and dir != 'left' and ((dir == 'right' and k < 10) or (dir != 'right' and k >= 4)):
            k_ = 1 if dir != 'right' else 1+k
            heappush(q, (loss + grid[x][y+1], x, y+1, k_, 'right'))

    return loss


print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))