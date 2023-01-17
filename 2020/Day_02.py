path = 'Advent_of_Code/2020/puzzle_input/02.txt'

with open(path) as input:
    pws = input.read().split('\n')

def get_valid_pws_1():
    count = 0
    for pw in pws:
        count_range, letter, pw = pw.split()
        lower, upper = count_range.split('-')
        count_range = range(int(lower), int(upper)+1)
        letter = letter.strip(':')
        if pw.count(letter) in count_range:
            count += 1
    return count

def get_valid_pws_2():
    count = 0
    for pw in pws:
        indices, letter, pw = pw.split()
        i, j = map(lambda x: int(x)-1, indices.split('-'))
        letter = letter.strip(':')
        if (pw[i] == letter and not pw[j] == letter) or (not pw[i] == letter and pw[j] == letter):
            count += 1
    return count

print(f'Part 1: {get_valid_pws_1()}')
print(f'Part 2: {get_valid_pws_2()}')