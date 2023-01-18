path = 'Advent_of_Code/2016/puzzle_input/01.txt'

with open(path) as input:
    instructions = input.read().split(', ')

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # North, East, South, West

x = y = 0   # starting out at (0, 0)
d = 0       # starting out facing north

visited = set()
visited_twice = None 

for ins in instructions:
    turn, dist = ins[0], int(ins[1:])
    if turn == 'R':
        d = (d + 1) % 4
    else:
        d = (d - 1) % 4
        
    i, j = directions[d]
    for _ in range(dist):
        x += i
        y += j
        if not visited_twice and (x, y) in visited:
            visited_twice = abs(x) + abs(y)
        visited.add((x, y))

bunny_HQ = abs(x) + abs(y)

print(f'Part 1: {bunny_HQ}')
print(f'Part 2: {visited_twice}')