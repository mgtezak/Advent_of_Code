with open('Advent_of_Code/2022/puzzle_input/06.txt') as input:
    data = input.read()

def solve(part2=False):
    l = 14 if part2 else 4
    for i in range(l, len(data) + 1):
        if len(set(data[i-l:i])) == l:
            return i
        
print(f'Part 1: {solve()}')
print(f'Part 2: {solve(part2=True)}')