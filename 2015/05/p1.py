def part1(puzzle_input):

    def contains_three_vowels(s):
        count = sum([s.count(v) for v in 'aeiou'])
        if count >= 3:
            return True

    def contains_double(s):
        if any(s[i] == s[i+1] for i in range(len(s) - 1)):
            return True

    def contains_naughty(s):
        if any(x in s for x in ['ab', 'cd', 'pq', 'xy']):
            return True    

    def is_nice(s):
        return (
            contains_three_vowels(s) and
            contains_double(s) and
            not contains_naughty(s)
        )

    return sum(1 for s in puzzle_input.split() if is_nice(s))
