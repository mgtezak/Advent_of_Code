path = 'Advent_of_Code/2019/puzzle_input/04.txt'

with open(path) as input:
    data = input.read()

def passes(n, part2=False):   
    s = str(n)
    if any(int(s[i]) > int(s[i+1]) for i in range(5)):
        return False
    groups = [s.count(digit) for digit in set(s)]
    return 2 in groups if part2 else max(groups) >= 2

start, end = [int(n) for n in data.split('-')]
r = range(start, end)

part1 = len([n for n in r if passes(n)])
part2 = len([n for n in r if passes(n, part2=True)])

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')