with open('Advent_of_Code/2022/puzzle_input/10.txt') as input:
    lines = [line.split() for line in input.read().split('\n')]

cycle = 0
x = 1
sum_of_signal_strengths = 0
row = 0
image = ['' for _ in range(6)]

for line in lines:
    for _ in range(len(line)):
        cycle += 1
        if cycle == 41:
            cycle -= 40
            row += 1
        if cycle == 20:
            sum_of_signal_strengths += x * (cycle + 40 * row)
        image[row] += '#' if x in range(cycle-2, cycle+1) else '.'
    if line[0] == 'addx':
        x += int(line[1])

image = '\n' + '\n'.join(image)

print(f'Part 1: {sum_of_signal_strengths}')
print(f'Part 2: {image}')