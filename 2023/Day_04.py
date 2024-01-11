import re

with open('Advent_of_Code/2023/puzzle_input/04.txt', 'r') as f:
    puzzle_input = f.read()


def part1(puzzle_input):
    regex = r':(.*)\|(.*)'
    points = 0
    for win_nums, true_nums in re.findall(regex, puzzle_input):
        overlap = set(win_nums.split()) & set(true_nums.split())
        if overlap:
            points += 2 ** (len(overlap) - 1)

    return points



def part2(puzzle_input):
    lines = puzzle_input.split('\n')
    regex = r':(.*)\|(.*)'
    cards = [1] * len(lines)
    for i, line in enumerate(lines):
        win_nums, actual_nums = re.findall(regex, line)[0]
        overlap = set(win_nums.split()) & set(actual_nums.split())
        for j in range(len(overlap)):
            cards[i+j+1] += cards[i]
    
    return sum(cards)



print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))