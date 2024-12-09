from string import ascii_letters

def part2(puzzle_input):

    def calc_remaining_len(del_letters: tuple=()) -> int:
        remaining = []
        for char in puzzle_input:
            if remaining and abs(ord(char) - ord(remaining[-1])) == 32:
                remaining.pop()
            elif char not in del_letters:
                remaining.append(char)
        return len(remaining)

    alphabet = ascii_letters
    return min(calc_remaining_len((alphabet[i], alphabet[i+26])) for i in range(26))