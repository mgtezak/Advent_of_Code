'''I created this interactive version of the Day 22 challenge as an alternative and hopefully more fun way of solving it.
It's basically a game that you can run in your terminal. The best scores achievable with my puzzle input are:
Part 1: 953
Part 2: 1289
Scroll all the way down to see some winning strategies.'''

import time
from dataclasses import dataclass

# from my puzzle input:
boss_hp = 55
boss_dmg = 8

# to make it flow a bit more:
sleep_time = 0.1

@dataclass
class InitialState:
    hard_mode: bool = False
    player_turn: int = 1
    poison: int = 0
    shield: int = 0
    recharge: int = 0
    mana: int = 500
    spent_mana: int = 0
    player_hp: int = 50
    boss_hp: int = boss_hp

def play_interactive_game(GameState: InitialState) -> int:
    turn = 'player' if GameState.player_turn == 1 else 'boss'

    print(f'    --- {turn} turn ---')
    time.sleep(sleep_time)
    print(f'    - player has {GameState.player_hp} hp')
    time.sleep(sleep_time)
    print(f'    - boss has {GameState.boss_hp} hp')
    time.sleep(sleep_time)
    
    if GameState.hard_mode and GameState.player_turn:
        GameState.player_hp -= 1
        print('    you lose 1 hp due to hard mode')
        time.sleep(sleep_time)
        if not GameState.player_hp:
            print('    ~~~~~~~~~~~~~~\n    you have 0 HP. you lose!\n')
            return

    if GameState.poison:
        GameState.poison -= 1
        print(f'    poison deals 3 damage, its timer is now {GameState.poison}!')
        time.sleep(sleep_time)
        GameState.boss_hp -= 3
        if GameState.boss_hp <= 0:
            print('    ~~~~~~~~~~~~~~\n    boss has 0 hp. you win!')
            time.sleep(sleep_time)
            print(f'    TOTAL MANA SPENT: {GameState.spent_mana}\n')
            return
    
    if GameState.shield:
        GameState.shield -= 1
        print(f'    shield\'s timer is now {GameState.shield}!')
        time.sleep(sleep_time)
   
    if GameState.recharge:
        GameState.mana += 101
        GameState.recharge -= 1
        print(f'    recharge provides 101 mana; its timer is now {GameState.recharge}!')
        time.sleep(sleep_time)
        
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
        time.sleep(sleep_time)
        for spell, cost in spells.items():
            print(f'    {spell}:      \t{cost}')
            time.sleep(sleep_time)
        spell = input('    choose spell: ')
        while spell not in spells:
            spell = input('    wrong input. try again. choose spell: ')
        time.sleep(sleep_time)
        print('    ~~~~~~~~~~~~~~')
        time.sleep(sleep_time)

        if spell == 'magic missle':
            print('    player casts magic missle dealing 4 damage!')
            time.sleep(sleep_time)
            GameState.boss_hp -= 4
            GameState.mana -= 53
            GameState.spent_mana += 53
        elif spell == 'drain':
            print('    player casts drain!')
            time.sleep(sleep_time)
            GameState.boss_hp -= 2
            GameState.player_hp += 2
            GameState.mana -= 73
            GameState.spent_mana += 73
        elif spell == 'shield':
            print('    player casts shield, increasing armor by 7!')
            time.sleep(sleep_time)
            GameState.shield = 6
            GameState.mana -= 113
            GameState.spent_mana += 113
        elif spell == 'poison':
            print('    player casts poison!')
            time.sleep(sleep_time)
            GameState.poison = 6
            GameState.mana -= 173
            GameState.spent_mana += 173
        elif spell == 'recharge':
            print('    player casts recharge!')
            time.sleep(sleep_time)
            GameState.recharge = 5
            GameState.mana -= 229
            GameState.spent_mana += 229
    
        if GameState.boss_hp <= 0:
            print('    ~~~~~~~~~~~~~~\n    boss has 0 HP. you win!')
            time.sleep(sleep_time)
            print(f'    TOTAL MANA SPENT: {GameState.spent_mana}\n')
            return
    
    if not GameState.player_turn:
        player_armor = 7 if GameState.shield else 0
        net_dmg = max(boss_dmg - player_armor, 1)
        GameState.player_hp -= net_dmg
        print(f'    ~~~~~~~~~~~~~~\n    boss attacks for {net_dmg} damage!')
        time.sleep(sleep_time)
        if GameState.player_hp <= 0:
            print('    ~~~~~~~~~~~~~~\n    you have 0 HP. you lose!\n')
            return
    
    time.sleep(sleep_time)
    print('          .')    
    time.sleep(sleep_time)
    print('          .')
    time.sleep(sleep_time)
    print('          .')
    time.sleep(sleep_time)
    
    GameState.player_turn = 1 - GameState.player_turn
    return play_interactive_game(GameState)

# Part 1:
print('\n    Play Game in Easy Mode')
time.sleep(sleep_time)
play_interactive_game(InitialState())
time.sleep(sleep_time*10)

# Part 2:
print('\n    Play Game in Hard Mode')
time.sleep(sleep_time)
play_interactive_game(InitialState(hard_mode=True))









'''Winning strategies are:
Part 1: shield, recharge, poison, magic missle, magic missle, poison, magic missle, magic missle, magic missle
Part 2: poison, recharge, shield, poison, recharge, drain, poison, drain, magic missle'''