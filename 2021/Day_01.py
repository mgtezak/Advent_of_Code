path = 'Advent_of_Code/2021/puzzle_input/01.txt'

with open(path) as input:
    measurements = list(map(int, input.read().split('\n')))

def get_increases(measurements):
    count = 0
    for i, m in enumerate(measurements):
        if i == 0:
            continue
        if m > measurements[i-1]:
            count += 1
    return count

windows = [sum(measurements[j] for j in (i-2, i-1, i)) for i in range(2, len(measurements))]

print(f'Part 1: {get_increases(measurements)}')
print(f'Part 2: {get_increases(windows)}')