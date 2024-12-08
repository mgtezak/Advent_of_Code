def part1(puzzle_input):
    lines = puzzle_input.split()

    def parse(lines):
        for line in lines:
            letters = ''.join(line.split('-')[:-1])
            sector_id = int(line.split('-')[-1].split('[')[0])
            checksum = line.split('[')[1].strip(']')
            yield letters, sector_id, checksum

    def get_true_checksum(letters):
        ranking = sorted((-letters.count(letter), letter) for letter in set(letters))
        return ''.join(letter for _, letter in ranking[:5])

    return sum(sector_id for letters, sector_id, checksum in parse(lines) if checksum == get_true_checksum(letters))