def part2(puzzle_input):
            
    def has_repeating_pair(s):
        if any(s[i:i+2] == s[j:j+2] for i in range(len(s)-3) for j in range(i+2, len(s)-1)):
            return True

    def repeats_after_gap(s):
        for i in range(len(s) - 2):
            if s[i] == s[i+2]:
                return True

    def is_nice(string):
        return has_repeating_pair(string) and repeats_after_gap(string)
        
    return sum(1 for s in puzzle_input.split() if is_nice(s))
