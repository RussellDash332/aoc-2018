import re
from copy import deepcopy

data = []
for _ in range(2):
    try:
        input()
        data.append([])
        while True:
            units, hp, stats, dmg, typ, init = re.findall('(\d+) units each with (\d+) hit points (\([\w\s;,]+\))?\s?with an attack that does (\d+) (\w+) damage at initiative (\d+)', input().strip())[0]
            units = int(units)
            hp = int(hp)
            dmg = int(dmg)
            init = int(init)
            stats = stats[1:-1].split('; ')
            new_stats = {'immune': [], 'weak': []}
            for stat in stats:
                if stat:
                    new_stats[stat.split()[0]].extend(stat[stat.find('to ')+3:].split(', '))
            cleaned = [units, hp, new_stats, dmg, typ, init]
            data[-1].append(cleaned)
    except:
        pass

def ep(grp):
    return grp[0] * grp[3]

def simulate(boost):
    immune, infection = deepcopy(data)
    for i in range(len(immune)):
        immune[i][3] += boost

    while immune and infection:
        infection = list(filter(lambda x: x[0] > 0, infection))
        immune = list(filter(lambda x: x[0] > 0, immune))

        if debug:
            print('Immune')
            for i in immune: print(i)
            print('Infection')
            for i in infection: print(i)
            print()

        attack, defend = infection, immune
        attacker, defender = 'infection', 'immune'
        attack.sort(key=lambda x: [ep(x), x[5]], reverse=True)
        defend.sort(key=lambda x: [ep(x), x[5]], reverse=True)

        seq = {'infection': {}, 'immune': {}}
        for _ in range(2):
            for i, (units, _, _, dpu, wpn, init_atk) in enumerate(attack):
                dmg = units * dpu
                choices = []
                for j, dfd in enumerate(defend):
                    stat, init_dfd = dfd[2], dfd[5]
                    if wpn in stat['immune'] or j in seq[attacker]: continue
                    elif wpn in stat['weak']:                       choices.append([2*dmg, ep(dfd), init_dfd, j, 2])
                    else:                                           choices.append([dmg, ep(dfd), init_dfd, j, 1])
                if choices:
                    choice = max(choices)
                    # seq[attacker][index_of_defender] = [attacker_init, damage, factor, index_of_attacker]
                    seq[attacker][choice[3]] = [init_atk, choice[0], choice[4], i]
            attack, defend = defend, attack
            attacker, defender = defender, attacker
        seq = [(k, *v, attacker) for k, v in seq[attacker].items()] + [(k, *v, defender) for k, v in seq[defender].items()]
        seq.sort(key=lambda x: -x[1])
        check = False
        for dfd_idx, _, _, factor, atk_idx, who in seq:
            if who == 'infection':
                target = immune[dfd_idx]
                by = infection[atk_idx]
            elif who == 'immune':
                target = infection[dfd_idx]
                by = immune[atk_idx]
            if by[0] > 0:
                if ep(by) * factor // target[1] > 0:
                    check = True
                target[0] -= ep(by) * factor // target[1]
        if not check:
            break
    return infection, immune

debug = False
infection, immune = simulate(0)
print('Part 1:', sum([x[0] for x in infection + immune]))

debug = False
infection, immune = [1], []
boost = 0
while infection or not immune:
    infection, immune = simulate(boost)
    boost += 1
print('Part 2:', sum([x[0] for x in infection + immune]))