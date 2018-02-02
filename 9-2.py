from itertools import permutations

a = open('9.txt').read().split('\n')

cities = set()
distances = {x.split(' = ')[0]: int(x.split(' = ')[1]) for x in a}

for x in a:
    cities |= set(x.split(' = ')[0].split(' to '))

maximum = 0

def get_distance(a, b):
    if ' to '.join([a, b]) in distances:
        return distances[' to '.join([a, b])]
    elif ' to '.join([b, a]) in distances:
        return distances[' to '.join([b, a])]
    else:
        return None

for x in permutations(cities):
    local_maximum = 0
    for i in range(len(x) - 1):
        distance = get_distance(x[i], x[i + 1])
        if distance != None:
            local_maximum += distance
        else:
            break
    maximum = max([maximum, local_maximum])

print maximum