import re


def part1(puzzle_input):
    regex = r':(.*)\|(.*)'
    points = 0
    
    for win_nums, true_nums in re.findall(regex, puzzle_input):
        overlap = set(win_nums.split()) & set(true_nums.split())
        if overlap:
            points += 2 ** (len(overlap) - 1)

    return points
