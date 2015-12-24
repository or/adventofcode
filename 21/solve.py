#!/usr/bin/python3


# cost, damage, armor
shop_weapons = {
    'Dagger': (8, 4, 0),
    'Shortsword': (10, 5, 0),
    'Warhammer': (25, 6, 0),
    'Longsword': (40, 7, 0),
    'Greataxe': (74, 8, 0),
}

shop_armors = {
    'None': (0, 0, 0),
    'Leather': (13, 0, 1),
    'Chainmail': (31, 0, 2),
    'Splintmail': (53, 0, 3),
    'Bandedmail': (75, 0, 4),
    'Platemail': (102, 0, 5),
}

shop_rings = {
    'None': (0, 0, 0),
    'Damage +1': (25, 1, 0),
    'Damage +2': (50, 2, 0),
    'Damage +3': (100, 3, 0),
    'Defense +1': (20, 0, 1),
    'Defense +2': (40, 0, 2),
    'Defense +3': (80, 0, 3),
}

def strike(a, b):
    damage = max(1, a['damage'] - b['armor'])
    b['points'] -= damage

def fight(config):
    player = {'points': 100}
    player.update(config)

    boss = {
        'points': 100,
        'damage': 8,
        'armor': 2,
    }

    while True:
        strike(player, boss)
        if boss['points'] <= 0:
            return True

        strike(boss, player)
        if player['points'] <= 0:
            return False

solution = None
for weapon, weapon_config in shop_weapons.items():
    for armor, armor_config in shop_armors.items():
        for ring1, ring1_config in shop_rings.items():
            for ring2, ring2_config in shop_rings.items():
                if ring1 == ring2 and ring1 != 'None':
                    continue

                setup = (weapon, armor, ring1, ring2)

                cost = sum([weapon_config[0], armor_config[0],
                            ring1_config[0], ring2_config[0]]),
                config = {
                    'damage':
                    sum([weapon_config[1], armor_config[1],
                         ring1_config[1], ring2_config[1]]),

                    'armor':
                    sum([weapon_config[2], armor_config[2],
                         ring1_config[2], ring2_config[2]]),
                }

                if solution and cost >= solution[0]:
                    continue

                if fight(config):
                    solution = (cost, config, setup)

print(solution)

solution = None
for weapon, weapon_config in shop_weapons.items():
    for armor, armor_config in shop_armors.items():
        for ring1, ring1_config in shop_rings.items():
            for ring2, ring2_config in shop_rings.items():
                if ring1 == ring2 and ring1 != 'None':
                    continue

                setup = (weapon, armor, ring1, ring2)

                cost = sum([weapon_config[0], armor_config[0],
                            ring1_config[0], ring2_config[0]]),
                config = {
                    'damage':
                    sum([weapon_config[1], armor_config[1],
                         ring1_config[1], ring2_config[1]]),

                    'armor':
                    sum([weapon_config[2], armor_config[2],
                         ring1_config[2], ring2_config[2]]),
                }

                if solution and cost < solution[0]:
                    continue

                if not fight(config):
                    solution = (cost, config, setup)

print(solution)
