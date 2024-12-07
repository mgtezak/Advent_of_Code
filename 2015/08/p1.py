import ast

def part1(puzzle_input):
    str_chars = 0
    for line in puzzle_input.split():
        if line[0] != '"' or line[-1] != '"': # checking if there's no danger in using literal eval 
            raise ValueError("Invalid puzzle input.")      
        str_chars += len(line) - len(ast.literal_eval(line))
    return str_chars