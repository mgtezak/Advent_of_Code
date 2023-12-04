import re

with open('Advent_of_Code/2023/puzzle_input/04.txt', 'r') as f:
    puzzle_input = f.read()


def part1(puzzle_input):
    regex = r':(.*?)\|(.*)'
    points = 0
    for line in puzzle_input.split('\n'):
        nums = re.search(regex, line)
        win_nums = set(map(int, nums.group(1).split()))
        true_nums = set(map(int, nums.group(2).split()))
        n_matches = len(win_nums & true_nums)
        if n_matches:
            points += 2 ** (n_matches - 1)

    return points


def part2(puzzle_input):
    lines = puzzle_input.split('\n')
    cards = [1] * len(lines)
    regex = r':(.*?)\|(.*)'
    for i, line in enumerate(lines):
        nums = re.search(regex, line)
        win_nums = set(map(int, nums.group(1).split()))
        true_nums = set(map(int, nums.group(2).split()))
        n_matches = len(win_nums & true_nums)
        for j in range(i + 1, i + 1 + n_matches):
            cards[j] += cards[i]
    
    return sum(cards)


print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))