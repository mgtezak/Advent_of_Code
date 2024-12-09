def part1(puzzle_input):
    nums = list(map(int, puzzle_input.split()))

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

    return parse(nums)[0]