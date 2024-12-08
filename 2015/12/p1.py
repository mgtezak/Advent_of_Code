import json


def part1(puzzle_input):

    def sum_of_item(item):

        if type(item) == list:
            return sum([sum_of_item(i) for i in item])

        if type(item) == dict:
            return sum([sum_of_item(i) for i in item.values()])

        if type(item) == str:
            return 0

        if type(item) == int:
            return item
        
    doc = json.loads(puzzle_input)
    return sum_of_item(doc)
