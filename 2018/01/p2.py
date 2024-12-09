def part2(puzzle_input):
    nums = [int(line) for line in puzzle_input.split('\n')]
    past_frequencies = {0}
    current_freq = 0
    while True:
        for n in nums:
            current_freq += n
            if current_freq in past_frequencies:
                return current_freq
            past_frequencies.add(current_freq)