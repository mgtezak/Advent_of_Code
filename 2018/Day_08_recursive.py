path = 'Advent_of_Code/2018/puzzle_input/08.txt'

with open(path) as input:
    nums = list(map(int, input.read().split()))

def parse(nums):
    n_children, n_metadata = nums[:2]
    nums = nums[2:]
    total = 0

    if n_children:
        vals = []
        for _ in range(n_children):
            t, v, nums = parse(nums)
            total += t
            vals.append(v)

        val = sum(vals[i-1] for i in nums[:n_metadata] if i-1 in range(len(vals)))

    else:
        val = sum(nums[:n_metadata])

    total += sum(nums[:n_metadata])

    return total, val, nums[n_metadata:]

total, val, _ = parse(nums)


print(f'Part 1: {total}')
print(f'Part 2: {val}')