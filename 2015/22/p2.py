from dataclasses import dataclass
import re
import random


def part2(puzzle_input, is_example_input=False):
    """
    I'm kind of brute forcing it by playing the game a very large number of times 
    (500_000 seems to do the trick) using a completely random strategy. 
    Maybe not the most elegant or efficient solution.
    """

    boss_hp, boss_dmg = map(int, re.findall(r'(\d+)', puzzle_input))

    @dataclass
    class GameState:
        hard_mode: bool
        best_score: int
        boss_hp: int
        player_turn: int = 1
        poison: int = 0
        shield: int = 0
        recharge: int = 0
        mana: int = 250 if is_example_input else 500
        spent_mana: int = 0
        player_hp: int = 10 if is_example_input else 50
        

    def play_game(s: GameState) -> int | bool:
        if s.poison > 0:
            s.poison -= 1
            s.boss_hp -= 3
            if s.boss_hp <= 0:  # Player wins!
                return s.spent_mana
        
        if s.shield > 0:
            s.shield -= 1
    
        if s.recharge > 0:
            s.mana += 101
            s.recharge -= 1
            
        if s.player_turn:
            if s.hard_mode:
                s.player_hp -= 1
                if not s.player_hp:  # Boss wins!
                    return False

            while True:
                spell = random.choice(['magic missle', 'drain', 'shield', 'poison', 'recharge'])

                if spell == 'magic missle':
                    cost = 53
                    if s.mana < cost:
                        return False
                    s.boss_hp -= 4

                elif spell=='drain':
                    cost = 73
                    if s.mana < cost:
                        continue
                    s.boss_hp -= 2
                    s.player_hp += 2

                elif spell=='shield':
                    cost = 113
                    if s.mana < cost or s.shield:
                        continue
                    s.shield = 6

                elif spell=='poison':
                    cost = 173
                    if s.mana < cost or s.poison:
                        continue
                    s.poison = 6

                elif spell=='recharge':
                    cost = 229
                    if s.mana < cost or s.recharge:
                        continue
                    s.recharge = 5

                break
            
            s.mana -= cost
            s.spent_mana += cost
            if s.best_score and s.spent_mana > s.best_score:
                return False  # Might still win but not optimally
            
            if s.boss_hp <= 0:
                return s.spent_mana  # Player wins!
        
        else:  # Boss' turn
            player_armor = 7 if s.shield else 0
            s.player_hp -= max(boss_dmg - player_armor, 1)

            if s.player_hp <= 0:  # Boss wins!
                return False

        s.player_turn = 1 - s.player_turn
        return play_game(s)

    best_score = None
    for _ in range(500_000):
        score = play_game(GameState(hard_mode=True, best_score=best_score, boss_hp=boss_hp))
        if score and (best_score is None or best_score > score):
            best_score = score
        
    return best_score
