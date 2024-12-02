def part2(puzzle_input):        

    def is_safe(nums, safe_range, allow_skip):
        prev = nums[0]
        for curr in nums[1:]:
            if curr - prev in safe_range:
                prev = curr
            elif not allow_skip:
                return False
            else:
                allow_skip = False
        return True
    
    safe = 0
    increasing = range(1, 4)
    decreasing = range(-3, 0)
    for line in puzzle_input.split('\n'):
        nums = [int(num) for num in line.split()]
        safe += any([
            is_safe(nums, increasing, True), 
            is_safe(nums, decreasing, True),
            is_safe(nums[1:], increasing, False),
            is_safe(nums[1:], decreasing, False)
        ])

    return safe
