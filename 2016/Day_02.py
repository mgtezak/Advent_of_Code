path = 'Advent_of_Code/2016/puzzle_input/02.txt'

with open(path) as input:
    lines = input.read().split()

# Part 1:

keypad_1 = ['123', '456', '789']

bathroom_code_1 = []
for line in lines:
    x = y = 1
    for char in line:
        if char == 'L':
            x -= 1 if x > 0 else 0
        elif char == 'R':            
            x += 1 if x < 2 else 0
        elif char == 'U':
            y -= 1 if y > 0 else 0
        elif char == 'D':           
            y += 1 if y < 2 else 0
    bathroom_code_1.append(str(keypad_1[y][x]))


# Part 2:

keypad_2 = ['  1  ', ' 234 ', '56789', ' ABC ', '  D  ']

bathroom_code_2 = []
for line in lines:
    x, y = 0, 2    # start at position of '5'
    for char in line:
        if char == 'L':
            x -= 1 if x > 0 and keypad_2[y][x-1] != ' ' else 0
        elif char == 'R':            
            x += 1 if x < 4 and keypad_2[y][x+1] != ' ' else 0
        elif char == 'U':
            y -= 1 if y > 0 and keypad_2[y-1][x] != ' ' else 0
        elif char == 'D':           
            y += 1 if y < 4 and keypad_2[y+1][x] != ' ' else 0
    bathroom_code_2.append(keypad_2[y][x])


print(f'Part 1: {"".join(bathroom_code_1)}')
print(f'Part 2: {"".join(bathroom_code_2)}')