import re

regex = r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)'
with open('Advent_of_Code/2015/puzzle_input/16.txt') as input:
    sues = {int(i): {a: int(b), c: int(d), e: int(f)} for i, a, b, c, d, e, f in re.findall(regex, input.read())}

evidence = '''children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1'''
evidence = {line.split(': ')[0]: int(line.split(': ')[1]) for line in evidence.split('\n')}

def find_sue_1():
    for i in sues:
        for item in sues[i]:
            if sues[i][item] != evidence[item]:
                break
        else:
            return i
            
def find_sue_2():
    for i in sues:
        for item in sues[i]:
            if item in ('cats', 'trees') and sues[i][item] <= evidence[item]:
                break
            elif item in ('pomeranians', 'goldfish') and sues[i][item] >= evidence[item]:
                break
            elif item not in ('cats', 'trees', 'pomeranians', 'goldfish') and sues[i][item] != evidence[item]:
                break
        else:
            return i

print(f'Part 1: {find_sue_1()}')
print(f'Part 2: {find_sue_2()}')