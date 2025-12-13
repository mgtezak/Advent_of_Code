from itertools import count

def part1(puzzle_input):
    total_presses = 0
    for line in puzzle_input.splitlines():
        target, *buttons, _ = line.split()
        target = sum(1 << i for i, char in enumerate(target[1:-1]) if char == "#")
        buttons = [sum(1 << int(num) for num in btn[1:-1].split(',')) for btn in buttons]
        current_lights = {0}
        for presses in count(1):
            current_lights = set(lights ^ btn for lights in current_lights for btn in buttons)
            if target in current_lights:
                total_presses += presses
                break
            
    return total_presses
