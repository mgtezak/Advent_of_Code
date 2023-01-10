with open('Advent_of_Code/2022/puzzle_input/07.txt') as input:
    lines = [line.split() for line in input.read().split('\n')]

dir_size = {'root': 0}
for line in lines:
    if line[:2] == ['$', 'cd']:
        if line[2] == '/': 
            path = ['root']
        elif line[2] == '..': 
            path.pop()
        else:
            path.append(path[-1] + '/' + line[2])
            dir_size[path[-1]] = 0
    elif line[0].isnumeric():
        for p in path: 
            dir_size[p] += int(line[0]) 

one = sum([val for val in dir_size.values() if val <= 100_000])
two = sorted([v for v in dir_size.values() if v >= dir_size['root'] - 40_000_000])[0]

print(f'Part 1: {one}')
print(f'Part 2: {two}')