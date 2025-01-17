def part1(puzzle_input):
    lines = [line.split() for line in puzzle_input.split('\n')]
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

    return sum([val for val in dir_size.values() if val <= 100_000])
