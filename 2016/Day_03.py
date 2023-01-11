path = 'Advent_of_Code/2016/puzzle_input/03.txt'

with open(path) as input:
    lines = [list(map(int, line.split())) for line in input.read().split('\n')]

def validate(triangle):
    half = sum(triangle) / 2
    return True if all(s < half for s in triangle) else False

part1 = sum(validate(triangle) for triangle in lines)
part2 = sum(validate((lines[i][j], lines[i+1][j], lines[i+2][j])) for i in range(0, len(lines), 3) for j in range(3))

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')