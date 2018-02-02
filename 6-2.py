a = open('6.txt').read().split('\n')

actions = {'turn on': lambda x: x + 1, 'turn off': lambda x: max(x - 1, 0), 'toggle': lambda x: x + 2}

def modify(act, g, c1, c2):
    for y in range(c1[1], c2[1] + 1):
        for x in range(c1[0], c2[0] + 1):
            g[y][x] = actions[act](g[y][x])
    return g

g = [[0 for _ in xrange(1000)] for _ in xrange(1000)]

for x in a:
    x = x.split(' through ')
    act = ' '.join(x[0].split()[:-1])
    c1 = map(int, x[0].split()[-1].split(','))
    c2 = map(int, x[1].split(','))
    g = modify(act, g, c1, c2)

print sum([sum(x) for x in g])