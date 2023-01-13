path = 'Advent_of_Code/2017/puzzle_input/04.txt'

with open(path) as input:
    lines = [line.split() for line in input.read().split('\n')]
    lines2 = [[''.join(sorted(word)) for word in line] for line in lines]

def get_valid_passphrases(lines):
    return sum(len(set(line)) == len(line) for line in lines)

print(f'Part 1: {get_valid_passphrases(lines)}')
print(f'Part 2: {get_valid_passphrases(lines2)}')