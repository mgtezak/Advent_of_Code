import random
import re


def part2(puzzle_input):

    def get_score(recipe: list) -> int:
        '''calculate total score of cookie'''
        capacity = sum([recipe[i] * lines[i][0] for i in range(4)])
        durability = sum([recipe[i] * lines[i][1] for i in range(4)])
        flavor = sum([recipe[i] * lines[i][2] for i in range(4)])
        texture = sum([recipe[i] * lines[i][3] for i in range(4)])
        score = capacity * durability * flavor * texture
        return score

    def make_child_recipe(recipe: list) -> list:
        '''Alter recipe by randomly adding and removing 10 teaspoons of ingredients.'''
        child = recipe.copy()
        for _ in range(5):
            child[random.randint(0, 1)] += 1
        for _ in range(5):
            child[random.randint(0, 1)] -= 1
        for _ in range(5):
            child[random.randint(2, 3)] += 1
        for _ in range(5):
            child[random.randint(2, 3)] -= 1  
        return child

    def improve_recipe(parent: list) -> list:
        '''Compare parent recipe and 5 of its children and return the one with the best score'''
        recipes =  [parent] + [make_child_recipe(parent) for _ in range(5)]
        best_recipe = max(recipes, key=lambda r: get_score(r))
        return best_recipe

    lines = [list(map(int, re.findall(r'(-?\d)', line))) for line in puzzle_input.split('\n')]
    recipe = [30, 30, 20, 20]
    for _ in range(100):
        recipe = improve_recipe(recipe)

    return get_score(recipe)