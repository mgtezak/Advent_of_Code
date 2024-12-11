def part2(puzzle_input):

    def validate_num(n, prev):
        for i, n1 in enumerate(prev):
            for _, n2 in enumerate(prev[i+1:]):
                if n == n1 + n2:
                    return True
                
    nums = list(map(int, puzzle_input.split('\n')))
    for i, n in enumerate(nums):
        if i < 25:
            continue
        prev = nums[i-25:i]
        if not validate_num(n, prev):
            invalid_num = n
            break

    for i in range(nums.index(invalid_num)):
        j = i + 1
        while sum(nums[i:j]) < invalid_num:
            j += 1
        if sum(nums[i:j]) == invalid_num:
            return min(nums[i:j]) + max(nums[i:j])