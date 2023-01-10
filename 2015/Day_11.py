import string
import re

# my puzzle input:
pw = 'hepxcrrq'  

def check_pw(pw):
    ''' checks whether pw has two non-overlapping repeated letters and an alphabetical straight'''
    if len(re.findall(r'([a-z])\1', pw)) >= 2 and any(pw[i:i+3] in alphabet for i in range(6)):
        return True
    
def increment(pw):
    '''alphabetically increments pw from right to left'''
    pw = list(pw)
    for i in range(7, -1, -1):
        next_index = (altered_alphabet.index(pw[i]) + 1) % 23
        pw[i] = altered_alphabet[next_index]
        if pw[i] != 'a':
            return ''.join(pw)

def get_next(pw):
    '''increments pw until it finds a valid one'''
    while not check_pw(pw):
        pw = increment(pw)
    return pw

alphabet = string.ascii_lowercase
altered_alphabet = re.sub('[iol]', '', alphabet) # removing forbidden letters

part1 = get_next(pw)
part2 = get_next(increment(part1))

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')