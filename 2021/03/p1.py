def part1(puzzle_input):
    nums = puzzle_input.split('\n')
    gamma = ''
    for i in range(12):
        if sum(int(nums[j][i]) for j in range(len(nums))) < len(nums)/2:
            gamma += '0'
        else:
            gamma += '1'
    epsilon = ''.join(str(1-int(x)) for x in gamma)
    return int(gamma, 2) * int(epsilon, 2)