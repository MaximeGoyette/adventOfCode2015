a = open('6.txt').read().split('\n')

def turn_on(g, c1, c2):
    for y in range(c1[1], c2[1] + 1):
        for x in range(c1[0], c2[0] + 1):
            g[y][x] += 1
    return g

def turn_off(g, c1, c2):
    for y in range(c1[1], c2[1] + 1):
        for x in range(c1[0], c2[0] + 1):
            g[y][x] = max(g[y][x] - 1, 0)
    return g

def toggle(g, c1, c2):
    for y in range(c1[1], c2[1] + 1):
        for x in range(c1[0], c2[0] + 1):
            g[y][x] += 2
    return g

actions = {'turn on': turn_on, 'turn off': turn_off, 'toggle': toggle}

g = [[0 for _ in xrange(1000)] for _ in xrange(1000)]

for x in a:
    x = x.split(' through ')
    act = ' '.join(x[0].split()[:-1])
    c1 = map(int, x[0].split()[-1].split(','))
    c2 = map(int, x[1].split(','))
    g = actions[act](g, c1, c2)

print sum([sum(x) for x in g])