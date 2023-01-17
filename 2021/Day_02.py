path = 'Advent_of_Code/2021/puzzle_input/02.txt'

with open(path) as input:
    movements = [(m.split()[0], int(m.split()[1])) for m in input.read().split('\n')]

# Part1:
x = y = 0
for c, n in movements:
    if c == 'forward':
        x += n
    elif c == 'up':
        y -= n
    elif c == 'down':
        y += n

part1 = x * y

# Part 2:
x = y = aim = 0
for c, n in movements:
    if c == 'forward':
        x += n
        y += aim * n
    elif c == 'up':
        aim -= n
    elif c == 'down':
        aim += n

part2 = x * y

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')