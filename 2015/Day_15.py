import random
import re

with open('Advent_of_Code/2015/puzzle_input/15.txt') as input:
    lines = [list(map(int, re.findall('(-?\d)', line))) for line in input.readlines()]

def get_score(recipe: list) -> int:
    '''calculate total score of cookie'''
    capacity = sum([recipe[i] * lines[i][0] for i in range(len(lines))])
    durability = sum([recipe[i] * lines[i][1] for i in range(len(lines))])
    flavor = sum([recipe[i] * lines[i][2] for i in range(len(lines))])
    texture = sum([recipe[i] * lines[i][3] for i in range(len(lines))])
    score = capacity * durability * flavor * texture
    return score

def make_child_recipe(recipe: list, calories_count: bool=False) -> list:
    '''alter recipe by randomly adding and removing 10 teaspoons of ingredients'''
    child = recipe.copy()
    if calories_count == False:
        for _ in range(10):
            child[random.randint(0, 3)] += 1
        for _ in range(10):
            child[random.randint(0, 3)] -= 1
    else: # if calories matter then only the first two and the second two ingredients are interchangeable respectively
        for _ in range(5):
            child[random.randint(0, 1)] += 1
        for _ in range(5):
            child[random.randint(0, 1)] -= 1
        for _ in range(5):
            child[random.randint(2, 3)] += 1
        for _ in range(5):
            child[random.randint(2, 3)] -= 1  
    return child

def improve_recipe(recipe: list, calories_count: bool=False) -> list:
    '''create 5 children, score each and return the one with the best score'''
    children = [make_child_recipe(recipe, calories_count) for _ in range(5)]
    best_recipe = sorted([recipe] + children, key=lambda r: get_score(r)).pop()
    return best_recipe

def evolve_recipe(recipe: list, calories_count: bool=False, generations: int=100) -> int:
    '''evolve recipe 100 times'''
    recipe = improve_recipe(recipe, calories_count)
    if generations == 0:
        return get_score(recipe)
    return evolve_recipe(recipe, calories_count, generations-1)

starting_recipe = [30, 30, 20, 20]
part1 = evolve_recipe(starting_recipe, calories_count=False)
part2 = evolve_recipe(starting_recipe, calories_count=True)

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')