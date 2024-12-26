from functools import cache


def part1(puzzle_input):
    towels, designs =  puzzle_input.split('\n\n')
    towels = set(towels.split(', '))

    @cache
    def is_possible(design: str):
        return (
            design == '' 
            or any(
                design.startswith(towel) and 
                is_possible(design[len(towel):]) 
                for towel in towels
            )
        )
        
    return sum(map(is_possible, designs.split('\n')))
