with open('Advent_of_Code/2024/puzzle_input/02.txt', 'r') as f:
    puzzle_input = f.read()


def part1(puzzle_input):        

    def is_safe(seq, safe_range):
        for i in range(1, len(seq)):
            if seq[i] - seq[i-1] not in safe_range:
                return False
        return True
    
    safe = 0
    increasing = range(1, 4)
    decreasing = range(-3, 0)
    for line in puzzle_input.split('\n'):
        seq = [int(num) for num in line.split()]
        safe += is_safe(seq, increasing) or is_safe(seq, decreasing)

    return safe



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



print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))