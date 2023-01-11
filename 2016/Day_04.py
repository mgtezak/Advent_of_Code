path = 'Advent_of_Code/2016/puzzle_input/04.txt'

with open(path) as input:
    lines = input.read().split()

def parse(lines):
    for line in lines:
        letters = ''.join(line.split('-')[:-1])
        sector_id = int(line.split('-')[-1].split('[')[0])
        checksum = line.split('[')[1].strip(']')
        yield letters, sector_id, checksum

# Part 1:

def get_true_checksum(letters):
    ranking = sorted((-letters.count(letter), letter) for letter in set(letters))
    return ''.join(letter for _, letter in ranking[:5])

part1 = sum(sector_id for letters, sector_id, checksum in parse(lines) if checksum == get_true_checksum(letters))


# Part 2:

import string

def decrypt(letters, sector_id):
    shift = sector_id % 26
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    dictionary = str.maketrans(alphabet, shifted_alphabet)
    return letters.translate(dictionary)

part2 = [sector_id for letters, sector_id, _ in parse(lines) if 'northpole' in decrypt(letters, sector_id)][0]


print(f'Part 1: {part1}')
print(f'Part 2: {part2}')