import json

with open('Advent_of_Code/2015/puzzle_input/12.txt') as input:
    doc = json.load(input)

def sum_of_item(item, part2=False):

    if type(item) == list:
        return sum([sum_of_item(i, part2) for i in item])

    if type(item) == dict:
        if part2 and 'red' in item.values():
            return 0
        return sum([sum_of_item(i, part2) for i in item.values()])

    if type(item) == str:
        return 0

    if type(item) == int:
        return item

print(f'Part 1: {sum_of_item(doc)}')
print(f'Part 2: {sum_of_item(doc, part2=True)}')