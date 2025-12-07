def part1(puzzle_input):
    grid = puzzle_input.splitlines()
    beams = {grid[0].index('S')}
    splits = 0
    for row in grid[1:]:
        next_row_beams = set()
        for beam in beams:
            if row[beam] == '.':
                next_row_beams.add(beam)
            else:
                splits += 1
                next_row_beams |= {beam-1, beam+1}

        beams = next_row_beams

    return splits
