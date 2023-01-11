path = 'Advent_of_Code/2022/puzzle_input/18.txt'
with open(path) as input:
    lava_cubes = set(tuple(map(int, xyz.split(','))) for xyz in input.read().split('\n'))

adjacent = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
 
# part 1:
n_sides = sum(1 for x, y, z in lava_cubes for a, b, c in adjacent if (x+a, y+b, z+c) not in lava_cubes)

# part 2:

# # I used this to figure out dimensions for x, y, z:
# for i in range(3):
#     print(min(lava_cubes, key=lambda x: x[i])[i], max(lava_cubes, key=lambda x: x[i])[i])

# expand dimensions by one on each side:
dim = range(-1, 21)

n_visible_sides = 0
queue = [(0, 0, 0)]
visited = set()

# breadth-first-search algorhythm
while queue:
    x, y, z = queue.pop()
    visited.add((x, y, z))
    for a, b, c in adjacent:
        q, r, s = x+a, y+b, z+c
        if q in dim and r in dim and s in dim and not((q, r, s) in visited or (q, r, s) in queue):
            if (q, r, s) in lava_cubes:
                n_visible_sides += 1
            else:
                queue.append((q, r, s))

print(f'Part 1: {n_sides}')
print(f'Part 2: {n_visible_sides}')