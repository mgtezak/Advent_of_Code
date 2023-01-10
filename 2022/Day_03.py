import string

with open('Advent_of_Code/2022/puzzle_input/03.txt') as input:
    lines = [line for line in input.read().split()]

letters = ' ' + string.ascii_letters

# part 1 verbose:
part1 = 0
for line in lines:
    half = int(len(line)/2)
    first = line[:half]
    second = line[half:]
    for l in first:
        if l in second:
            part1 += letters.index(l)
            break

# part 1 as one-liner:
part1 = sum([letters.index([l for l in line[:int(len(line)/2)] if l in line[int(len(line)/2):]][0]) for line in lines])

# part 2 verbose:
part2 = 0
for i in range(0, len(lines), 3):
    for l in lines[i]:
        if l in lines[i+1] and l in lines[i+2]:
            part2 += letters.index(l)
            break

# part 2 as one-liner          
part2 = sum([letters.index([l for l in lines[i] if l in lines[i+1] and l in lines[i+2]][0]) for i in range(0, len(lines), 3)])

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')