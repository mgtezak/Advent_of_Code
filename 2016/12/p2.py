def part2(puzzle_input):
    lines = [line.split() for line in puzzle_input.split('\n')]
    registry = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
    i = 0 
    while i < len(lines):
        l = lines[i]
        if l[0] == 'cpy':
            registry[l[2]] = int(l[1]) if l[1].isnumeric() else registry[l[1]]
        elif l[0] == 'inc':
            registry[l[1]] += 1
        elif l[0] == 'dec':
            registry[l[1]] -= 1
        elif (l[1].isalpha() and registry[l[1]]) or (l[1].isnumeric() and l[1] != '0'):
            i += int(l[2]) - 1
        i += 1
    return registry['a']
