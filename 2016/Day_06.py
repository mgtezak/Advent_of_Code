with open('Advent_of_Code/2016/puzzle_input/06.txt') as input:
    lines = [line for line in input.read().split('\n')]

# Part 1:

msg_1 = ''
for i in range(8):
    letters = [line[i] for line in lines]
    most_freq = sorted((letters.count(l), l) for l in letters)[-1][1]
    msg_1 += most_freq


# Part 2:

msg_2 = ''
for i in range(8):
    letters = [line[i] for line in lines]
    least_freq = sorted((letters.count(l), l) for l in letters)[0][1]
    msg_2 += least_freq


print(f'Part 1: {msg_1}')
print(f'Part 2: {msg_2}')