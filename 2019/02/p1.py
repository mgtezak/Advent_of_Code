def part1(puzzle_input, is_example_input=False):
        nums = list(map(int, puzzle_input.split(',')))
        if not is_example_input:
            nums[1], nums[2] = 12, 2

        for i in range(len(nums)):
            val = nums[i]
            if i % 4 == 0:  
                if val == 1:
                    nums[nums[i+3]] = nums[nums[i+1]] + nums[nums[i+2]]
                elif val == 2:
                    nums[nums[i+3]] = nums[nums[i+1]] * nums[nums[i+2]]
                elif val == 99:
                    break
                
        return nums[0]
