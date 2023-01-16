path = 'Advent_of_Code/2018/puzzle_input/02.txt'

with open(path) as input:
    box_IDs = [line for line in input.read().split('\n')]

double = triple = 0
differ_by_1 = None

for i, b in enumerate(box_IDs):
    double += 1 if any(b.count(letter) == 2 for letter in b) else 0
    triple += 1 if any(b.count(letter) == 3 for letter in b) else 0
    
    if not differ_by_1:
        for other_b in box_IDs[i+1:]:
            differ = sum(1 if b[i] != other_b[i] else 0 for i, _ in enumerate(b))
            if differ == 1:
                differ_by_1 = {b, other_b}

a, b = differ_by_1
common_letters = ''.join(letter for i, letter in enumerate(a) if letter == b[i])

print(f'Part 1: {double * triple}')
print(f'Part 2: {common_letters}')