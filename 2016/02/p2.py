def part2(puzzle_input):
    keypad = ['  1  ', ' 234 ', '56789', ' ABC ', '  D  ']
    bathroom_code = []
    x, y = 0, 2    # start at position of '5'
    for line in puzzle_input.split():
        for char in line:
            if char == 'L':
                x -= 1 if x > 0 and keypad[y][x-1] != ' ' else 0
            elif char == 'R':            
                x += 1 if x < 4 and keypad[y][x+1] != ' ' else 0
            elif char == 'U':
                y -= 1 if y > 0 and keypad[y-1][x] != ' ' else 0
            elif char == 'D':           
                y += 1 if y < 4 and keypad[y+1][x] != ' ' else 0
        bathroom_code.append(keypad[y][x])

    return "".join(bathroom_code)
