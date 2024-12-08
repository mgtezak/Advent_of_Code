'''I created this interactive version of the Day 22 challenge as an alternative and hopefully more fun way of solving it.
It's basically a game that you can run in your terminal.

simply run:
`python interactive.py your_puzzle_input.txt`
or 
`python interactive.py your_puzzle_input.txt --hard`
for hard mode
'''

import time
from dataclasses import dataclass
import re
import argparse


@dataclass
class InitialState:
    boss_hp: int
    hard_mode: bool = False
    player_turn: bool = True
    poison: int = 0
    shield: int = 0
    recharge: int = 0
    mana: int = 500
    spent_mana: int = 0
    player_hp: int = 50
    
# to make the game flow a bit more:
def wait(t=0.1):
    time.sleep(t)

def play_interactive_game(GameState: InitialState, boss_dmg: int) -> int:
    turn = 'player' if GameState.player_turn else 'boss'

    print(f'    --- {turn} turn ---')
    wait()
    print(f'    - player has {GameState.player_hp} hp')
    wait()
    print(f'    - boss has {GameState.boss_hp} hp')
    wait()
    
    if GameState.hard_mode and GameState.player_turn:
        GameState.player_hp -= 1
        print('    you lose 1 hp due to hard mode')
        wait()
        if not GameState.player_hp:
            print('    ~~~~~~~~~~~~~~\n    you have 0 HP. you lose!\n')
            return

    if GameState.poison:
        GameState.poison -= 1
        print(f'    poison deals 3 damage, its timer is now {GameState.poison}!')
        wait()
        GameState.boss_hp -= 3
        if GameState.boss_hp <= 0:
            print('    ~~~~~~~~~~~~~~\n    boss has 0 hp. you win!')
            wait()
            print(f'    TOTAL MANA SPENT: {GameState.spent_mana}\n')
            return
    
    if GameState.shield:
        GameState.shield -= 1
        print(f'    shield\'s timer is now {GameState.shield}!')
        wait()

    if GameState.recharge:
        GameState.mana += 101
        GameState.recharge -= 1
        print(f'    recharge provides 101 mana; its timer is now {GameState.recharge}!')
        wait()
        
    if GameState.player_turn:
        spells = {}
        if GameState.mana >= 53:
            spells['magic missle'] = '53 mana'
        if GameState.mana >= 73:
            spells['drain'] = '73 mana'
        if GameState.mana >= 113 and not GameState.poison:
            spells['poison'] = '113 mana'
        if GameState.mana >= 173 and not GameState.shield:
            spells['shield'] = '173 mana'
        if GameState.mana >= 229 and not GameState.recharge:
            spells['recharge'] = '229 mana'
        
        if not spells:
            print('    ~~~~~~~~~~~~~~\n    not enough mana left. you lose!\n')
            return
        
        print(f'    ~~~~~~~~~~~~~~\n    with {GameState.mana} mana, here are your available spells:')
        wait()
        for spell, cost in spells.items():
            print(f'    {spell}:      \t{cost}')
            wait()
        spell = input('    choose spell: ')
        while spell not in spells:
            spell = input('    wrong input. try again. choose spell: ')
        wait()
        print('    ~~~~~~~~~~~~~~')
        wait()

        if spell == 'magic missle':
            print('    player casts magic missle dealing 4 damage!')
            wait()
            GameState.boss_hp -= 4
            GameState.mana -= 53
            GameState.spent_mana += 53
        elif spell == 'drain':
            print('    player casts drain!')
            wait()
            GameState.boss_hp -= 2
            GameState.player_hp += 2
            GameState.mana -= 73
            GameState.spent_mana += 73
        elif spell == 'shield':
            print('    player casts shield, increasing armor by 7!')
            wait()
            GameState.shield = 6
            GameState.mana -= 113
            GameState.spent_mana += 113
        elif spell == 'poison':
            print('    player casts poison!')
            wait()
            GameState.poison = 6
            GameState.mana -= 173
            GameState.spent_mana += 173
        elif spell == 'recharge':
            print('    player casts recharge!')
            wait()
            GameState.recharge = 5
            GameState.mana -= 229
            GameState.spent_mana += 229
    
        if GameState.boss_hp <= 0:
            print('    ~~~~~~~~~~~~~~\n    boss has 0 HP. you win!')
            wait()
            print(f'    TOTAL MANA SPENT: {GameState.spent_mana}\n')
            return
    
    if not GameState.player_turn:
        player_armor = 7 if GameState.shield else 0
        net_dmg = max(boss_dmg - player_armor, 1)
        GameState.player_hp -= net_dmg
        print(f'    ~~~~~~~~~~~~~~\n    boss attacks for {net_dmg} damage!')
        wait()
        if GameState.player_hp <= 0:
            print('    ~~~~~~~~~~~~~~\n    you have 0 HP. you lose!\n')
            return
    
    wait()
    print('          .')    
    wait()
    print('          .')
    wait()
    print('          .')
    wait()
    
    GameState.player_turn = not GameState.player_turn
    return play_interactive_game(GameState, boss_dmg)

def main():
    parser = argparse.ArgumentParser(description="Process a text file.")
    parser.add_argument('file', type=str, help='Path to the text file')
    parser.add_argument('--hard', action='store_true', help='Play the game in hard mode (default: False)')
    args = parser.parse_args()

    try:
        with open(args.file, 'r') as file:
            puzzle_input = file.read()
    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    boss_hp, boss_dmg = map(int, re.findall(r'(\d+)', puzzle_input))
    initial_state = InitialState(boss_hp=boss_hp, hard_mode=args.hard)
    play_interactive_game(initial_state, boss_dmg)


if __name__ == '__main__':
    main()


'''My winning strategies were:
Part 1: shield, recharge, poison, magic missle, magic missle, poison, magic missle, magic missle, magic missle
Part 2: poison, recharge, shield, poison, recharge, drain, poison, drain, magic missle'''