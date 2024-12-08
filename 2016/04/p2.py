import string


def part2(puzzle_input):
    lines = puzzle_input.split()

    def parse(lines):
        for line in lines:
            letters = ''.join(line.split('-')[:-1])
            sector_id = int(line.split('-')[-1].split('[')[0])
            checksum = line.split('[')[1].strip(']')
            yield letters, sector_id, checksum

    def decrypt(letters, sector_id):
        shift = sector_id % 26
        alphabet = string.ascii_lowercase
        shifted_alphabet = alphabet[shift:] + alphabet[:shift]
        dictionary = str.maketrans(alphabet, shifted_alphabet)
        return letters.translate(dictionary)

    return [sector_id for letters, sector_id, _ in parse(lines) if 'northpole' in decrypt(letters, sector_id)][0]