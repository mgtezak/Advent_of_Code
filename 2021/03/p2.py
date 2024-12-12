def part2(puzzle_input):

    nums = puzzle_input.split('\n')
    for i in range(12):
        vals = [n[i] for n in nums]
        if vals.count('0') > len(vals)/2:
            val = '0'
        else:
            val = '1'
        nums = [n for n in nums if n[i] == val]
        if len(nums) == 1:
            oxygen_generator = nums.pop()
            break

    nums = puzzle_input.split('\n')
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

    return int(oxygen_generator, 2) * int(co2_scrubber, 2)