import re


def part1(puzzle_input):
    possible = {'red': 12, 'green': 13, 'blue': 14}
    total = 0
    
    for id, game in enumerate(puzzle_input.split('\n'), start=1):
        for n, color in re.findall(r'(\d+) (red|green|blue)', game):
            if possible[color] < int(n):
                break
        else:
            total += id

    return total
