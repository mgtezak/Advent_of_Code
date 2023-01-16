path = 'Advent_of_Code/2018/puzzle_input/01.txt'

with open(path) as input:
    nums = [int(line) for line in input.read().split('\n')]

past_frequencies = {0}
current_freq = 0
duplicate = None
while not duplicate:
    for n in nums:
        current_freq += n
        if current_freq in past_frequencies:
            duplicate = current_freq
            break
        past_frequencies.add(current_freq)

print(f'Part 1: {sum(nums)}')
print(f'Part 2: {duplicate}')