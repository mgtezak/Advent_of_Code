from functools import cache


def part2(puzzle_input):
    towels, designs =  puzzle_input.split('\n\n')
    towels = set(towels.split(', '))

    @cache
    def count_ways(design: str):
        if not design:
            return 1
        
        combinations = 0
        for towel in towels:
            if design.startswith(towel):
                combinations += count_ways(design[len(towel):])

        return combinations
        
    return sum(map(count_ways, designs.split('\n')))
