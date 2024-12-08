import re


EQUIPS = '''\
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3\
'''

def part2(puzzle_input):

    # Parse input and equipment stats
    boss_hp, boss_dmg, boss_arm = map(int, re.findall(r'(\d+)', puzzle_input))

    equips = [[int(x) if x.isnumeric() else x for x in re.split(r'\s\s+', e)] for e in EQUIPS.split('\n')]

    weapons = equips[1:6]
    armor = equips[8:13]
    rings = equips[15:-1]

    armor.append(['No Armor', 0, 0, 0]) 
    rings.append(['No Ring', 0, 0, 0])

    def fight(player_dmg: int, player_arm: int, boss_hp: int=boss_hp) -> str:
        '''Simulates fight with given equipment and stats. Returns string about who wins.'''
        player_hp = 100
        player_net_dmg = player_dmg - boss_arm if player_dmg > 1 else 1
        boss_net_dmg = boss_dmg - player_arm if boss_dmg > player_arm else 1
        while True:
            boss_hp -= player_net_dmg
            if boss_hp <= 0:
                return 'player wins'
            player_hp -= boss_net_dmg
            if player_hp <= 0:
                return 'boss wins'

    # Get every possible equipment combination    
    equip_combs = []
    for w in weapons:
        for a in armor:
            for r1 in rings:
                for r2 in rings:
                    if r2 == r1 and r1[0] != 'No Ring':
                        continue
                    cost = w[1] + a[1] + r1[1] + r2[1]
                    dmg = w[2] + r1[2] + r2[2]
                    arm = a[3] + r1[3] + r2[3]
                    equip_combs.append((w, a, r1, r2, dmg, arm, cost))

    # Iterate through equipment combinations sorted by cost in reverse and return the most expensive
    for c in sorted(equip_combs, key=lambda x: -x[-1]):
        result = fight(c[4], c[5])
        if result == 'boss wins':
            break

    return c[-1]