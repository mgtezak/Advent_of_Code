with open('Advent_of_Code/2022/puzzle_input/02.txt') as input:
    lines = [line for line in input.read().split('\n')]

# Part 1:
points1 = 0
for line in lines:
    if line in ['A Y', 'B Z', 'C X']:
        points1 += 6
    elif line in ['A X', 'B Y', 'C Z']:
        points1 += 3 
    points1 += ['X', 'Y', 'Z'].index(line[-1]) + 1

# Part 2:
wins_against = {'s': 'r', 'r': 'p', 'p': 's'}
loses_against = {val: key for key, val in wins_against.items()}
points2 = 0
for line in lines:
    elf = ['r', 'p', 's'][['A', 'B', 'C'].index(line[0])]
    if line[-1] == 'Y':
        me = elf
        points2 += 3
    elif line[-1] == 'Z':
        me = wins_against[elf]
        points2 += 6
    else:
        me = loses_against[elf]
    points2 += ['r', 'p', 's'].index(me) + 1

print(f'Part 1: {points1}')
print(f'Part 2: {points2}')