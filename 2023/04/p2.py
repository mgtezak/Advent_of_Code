import re


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
