import hashlib

# my puzzle input:
key = 'iwrupvqb'

def solution(part2=False):
    num = 0
    while True:
        result = hashlib.md5((key + str(num)).encode())
        if (not part2 and result.hexdigest()[:5] == '00000') or (part2 and result.hexdigest()[:6] == '000000'):
            return num
        num += 1
        
print(f'Part 1: {solution()}')
print(f'Part 2: {solution(part2=True)}')

def solution(part2=False):
    num = 0
    while True:
        result = hashlib.md5((key + str(num)).encode())
        if (not part2 and result.hexdigest()[:5] == '00000') or (part2 and result.hexdigest()[:6] == '000000'):
            return num
        num += 1
        
print(f'Part 1: {solution()}')
print(f'Part 2: {solution(part2=True)}')