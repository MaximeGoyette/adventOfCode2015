p = open('11.txt').read()

al = 'abcdefghijklmnopqrstuvwxyz'

def rule1(p):
    for i in xrange(len(p) - 2):
        if p[i] == p[i + 1] - 1 and p[i + 1] == p[i + 2] - 1:
            return True
    return False

def rule2(p):
    return not bool(set(p).intersection(set([8, 11, 14])))

def rule3(p):
    s = set()
    for i in xrange(len(p) - 1):
        if p[i] == p[i + 1]:
            s.add(p[i])
    return len(s) >= 2

def get_next(p):
    p[-1] += 1
    for i in xrange(len(p) - 1, 0, -1):
        if p[i] == len(al):
            p[i] = 0
            p[i - 1] += 1
    return p

def get_next_valid(p):
    p = [al.index(x) for x in p]
    p = get_next(p)
    while not rule2(p) or not rule1(p) or not rule3(p):
        p = get_next(p)
    return ''.join([al[i] for i in p])

p = get_next_valid(p)
print get_next_valid(p)
