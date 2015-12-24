#!/usr/bin/python3


attacks = {
    'missile': {'cost': 53, 'damage': 4, 'heal': 0, 'armor': 0, 'mana': 0, 'times': 0},
    'drain': {'cost': 73, 'damage': 2, 'heal': 2, 'armor': 0, 'mana': 0, 'times': 0},
    'shield': {'cost': 113, 'damage': 0, 'heal': 0, 'armor': 7, 'mana': 0, 'times': 6},
    'poison': {'cost': 173, 'damage': 3, 'heal': 0, 'armor': 0, 'mana': 0, 'times': 6},
    'recharge': {'cost': 229, 'damage': 0, 'heal': 0, 'armor': 0, 'mana': 101, 'times': 5},
}

def solve(mana, player_points, boss_points, effects={}, used_mana=0, player_turn=True, hard=False):
    global min_solution, boss_damage
    if used_mana >= min_solution:
        return

    if hard and player_turn:
        player_points -= 1
        if player_points <= 0:
            return

    #print(used_mana, mana, player_points, boss_points, effects)
    player_armor = 0
    for effect in effects.values():
        player_points += effect['heal']
        player_armor += effect['armor']
        mana += effect['mana']
        boss_points -= effect['damage']
        effect['times'] -= 1

    if boss_points <= 0:
        min_solution = min(min_solution, used_mana)
        return

    effects_left = {key: dict(x) for key, x in effects.items() if x['times'] > 0}

    if not player_turn:
        player_points = player_points - max(boss_damage - player_armor, 1)
        if player_points <= 0:
            return

        solve(mana, player_points, boss_points, effects_left, used_mana, True, hard=hard)

    else:
        if mana < 53:
            return

        for attack, specs in attacks.items():
            if attack in effects_left or specs['cost'] > mana:
                continue

            tmp_used_mana = used_mana + specs['cost']
            tmp_mana = mana - specs['cost']
            tmp_effects = {key: dict(x) for key, x in effects_left.items()}

            tmp_player_points = player_points
            tmp_player_armor = player_armor
            tmp_boss_points = boss_points
            if specs['times'] == 0:
                tmp_player_points += specs['heal']
                tmp_player_armor += specs['armor']
                tmp_boss_points -= specs['damage']
                tmp_mana += specs['mana']
            else:
                tmp_effects[attack] = dict(specs)

            if tmp_boss_points <= 0:
                min_solution = min(min_solution, tmp_used_mana)
            else:
                solve(tmp_mana, tmp_player_points, tmp_boss_points, tmp_effects, tmp_used_mana, False, hard=hard)

min_solution = 100000000000000
player_mana = 500
player_points = 50
boss_points = 58
boss_damage = 9
#solve(player_mana, player_points, boss_points)
print(min_solution)

min_solution = 100000000000000
solve(player_mana, player_points, boss_points, hard=True)
print(min_solution)
