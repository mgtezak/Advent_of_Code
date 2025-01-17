def part1(puzzle_input):
    elves = []
    for elf in puzzle_input.split('\n\n'):
        elves.append(sum(map(int, elf.split('\n'))))
    return max(elves)