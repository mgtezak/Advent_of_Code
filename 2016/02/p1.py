def part1(puzzle_input):
    keypad = ['123', '456', '789']
    bathroom_code = []
    x = y = 1
    for line in puzzle_input.split():
        for char in line:
            if char == 'L':
                x -= 1 if x > 0 else 0
            elif char == 'R':            
                x += 1 if x < 2 else 0
            elif char == 'U':
                y -= 1 if y > 0 else 0
            elif char == 'D':           
                y += 1 if y < 2 else 0
        bathroom_code.append(str(keypad[y][x]))

    return int("".join(bathroom_code))
