path = 'Advent_of_Code/2017/puzzle_input/09.txt'

with open(path) as input:
    chars = input.read()

score = 0
level = 0
garbage = False
ignore_next = False
garbage_chars = 0   # part 2
for c in chars:
    if garbage:
        if ignore_next:
            ignore_next = False
        elif c == '!':
            ignore_next = True
        elif c == '>':
            garbage = False
        else:
            garbage_chars += 1   # part 2
    elif c == '{':
        level += 1
    elif c == '}':
        score += level
        level -= 1
    elif c == '<':
        garbage = True


print(f'Part 1: {score}')
print(f'Part 2: {garbage_chars}')