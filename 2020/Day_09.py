path = 'Advent_of_Code/2020/puzzle_input/09.txt'

with open(path) as input:
    nums = list(map(int, input.read().split('\n')))

# Part 1:

def validate_num(n, prev):
    for i, n1 in enumerate(prev):
        for _, n2 in enumerate(prev[i+1:]):
            if n == n1 + n2:
                return True

for i, n in enumerate(nums):
    if i < 25:
        continue
    prev = nums[i-25:i]
    if not validate_num(n, prev):
        invalid_num = n
        break


# Part 2

def find_encryption_weakness(target):
    for i in range(nums.index(target)):
        j = i + 1
        while sum(nums[i:j]) < target:
            j += 1
        if sum(nums[i:j]) == target:
            return min(nums[i:j]) + max(nums[i:j])
    

print(f'Part 1: {invalid_num}')
print(f'Part 2: {find_encryption_weakness(invalid_num)}')