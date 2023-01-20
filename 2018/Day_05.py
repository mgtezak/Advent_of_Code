path = 'Advent_of_Code/2018/puzzle_input/05.txt'

import string

with open(path) as input:
    polymer = input.read()

# part 1
def calc_remaining_len(del_letters: tuple=()) -> int:
    remaining = []
    for char in polymer:
        if remaining and abs(ord(char) - ord(remaining[-1])) == 32:
            remaining.pop()
        elif char not in del_letters:
            remaining.append(char)
    return len(remaining)

remaining_len = calc_remaining_len()


# part 2:
alphabet = string.ascii_letters
shortest_polymer = min(calc_remaining_len((alphabet[i], alphabet[i+26])) for i in range(26))


print(f'Part 1: {remaining_len}')
print(f'Part 2: {shortest_polymer}')