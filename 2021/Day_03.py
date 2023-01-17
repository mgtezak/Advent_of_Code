path = 'Advent_of_Code/2021/puzzle_input/03.txt'

with open(path) as input:
    nums = input.read().split('\n')

# Part 1:
gamma = ''
for i in range(12):
    if sum(int(nums[j][i]) for j in range(len(nums))) < len(nums)/2:
        gamma += '0'
    else:
        gamma += '1'

epsilon = ''.join(str(1-int(x)) for x in gamma)
power_consumption = int(gamma, 2) * int(epsilon, 2)

# Part 2:
nums_ = nums.copy()
for i in range(12):
    vals = [n[i] for n in nums_]
    if vals.count('0') > len(vals)/2:
        val = '0'
    else:
        val = '1'
    nums_ = [n for n in nums_ if n[i] == val]
    if len(nums_) == 1:
        oxygen_generator = nums_.pop()
        break

for i in range(12):
    vals = [n[i] for n in nums]
    if vals.count('0') > len(vals)/2:
        val = '1'
    else:
        val = '0'
    nums = [n for n in nums if n[i] == val]
    if len(nums) == 1:
        co2_scrubber = nums.pop()
        break

life_support = int(oxygen_generator, 2) * int(co2_scrubber, 2)

print(f'Part 1: {power_consumption}')
print(f'Part 2: {life_support}')