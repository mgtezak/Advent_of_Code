def part2(puzzle_input):        

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
        safe += any(
            is_safe(seq[:i] + seq[i+1:], safe_range) 
            for safe_range in (increasing, decreasing)
            for i in range(len(seq)) 
        )

    return safe
