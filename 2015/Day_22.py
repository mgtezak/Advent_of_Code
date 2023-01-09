'''I'm kind of brute forcing it by playing the game a very large number of times (500_000 seems to do the trick)  
using a completely random strategy. Maybe not the most elegant or efficient solution. I have two other approaches in mind:
    
1) A depth-first-search algorhythm that explores all possible strategies systematically.
2) A machine-learning based approach that starts out with a random strategy, and improves on it 
gradually through the creation, evaluation and selection of random mutations.'''

import random
from dataclasses import dataclass


with open('Advent_of_Code/2015/puzzle_input/22.txt') as input:
    boss_stats = [int(s.split(': ')[1]) for s in input.read().split('\n')]
    boss_hp, boss_dmg = boss_stats


@dataclass
class InitialState:
    hard_mode: bool
    best_score: int
    player_turn: int = 1
    poison: int = 0
    shield: int = 0
    recharge: int = 0
    mana: int = 500
    spent_mana: int = 0
    player_hp: int = 50
    boss_hp: int = boss_hp
    

def play_game(GameState: InitialState) -> int:
    player_armor = 0 if GameState.shield == 0 else 7

    if GameState.poison > 0:
        GameState.poison -= 1
        GameState.boss_hp -= 3
        if GameState.boss_hp <= 0:
            return GameState.spent_mana
    
    if GameState.shield > 0:
        GameState.shield -= 1
   
    if GameState.recharge > 0:
        GameState.mana += 101
        GameState.recharge -= 1
        
    if GameState.player_turn:
        if GameState.hard_mode:
            GameState.player_hp -= 1
            if not GameState.player_hp:
                return False
    
        while True:
            spell = random.choice(['magic missle', 'drain', 'shield', 'poison', 'recharge'])

            if spell == 'magic missle':
                cost = 53
                if GameState.mana < cost:
                    return False
                GameState.boss_hp -= 4

            elif spell=='drain':
                cost = 73
                if GameState.mana < cost:
                    continue
                GameState.boss_hp -= 2
                GameState.player_hp += 2

            elif spell=='shield':
                cost = 113
                if GameState.mana < cost:
                    continue
                GameState.shield = 6

            elif spell=='poison':
                cost = 173
                if GameState.mana < cost:
                    continue
                GameState.poison = 6

            elif spell=='recharge':
                cost = 229
                if GameState.mana < cost:
                    continue
                GameState.recharge = 5

            break
        
        GameState.mana -= cost
        GameState.spent_mana += cost
        if GameState.best_score and GameState.spent_mana > GameState.best_score:
            return False

        if GameState.boss_hp <= 0:
            return GameState.spent_mana
    
    if not GameState.player_turn:
        GameState.player_hp -= max(boss_dmg - player_armor, 1)

        if GameState.player_hp <= 0:
            return False

    GameState.player_turn = 1 - GameState.player_turn
    return play_game(GameState)

def play_n_games(n, hard_mode=False):
    best_score = None
    for _ in range(n):
        score = play_game(InitialState(hard_mode=hard_mode, best_score=best_score))
        if score and (not best_score or best_score > score):
            best_score = score
        
    return best_score

print(f'Part 1: {play_n_games(500_000)}')
print(f'Part 2: {play_n_games(500_000, hard_mode=True)}')