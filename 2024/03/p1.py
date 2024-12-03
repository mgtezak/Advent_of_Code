import re

def part1(puzzle_input):
    total = 0
    for a, b in re.findall(r"mul\((\d+),(\d+)\)", puzzle_input):
        total += int(a) * int(b)
        
    return total
