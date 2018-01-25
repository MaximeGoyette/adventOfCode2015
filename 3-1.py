a = open('3.txt').read()

d = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}

sc = (0, 0)

s = set([sc])

for x in a:
    sc = (sc[0] + d[x][0], sc[1] + d[x][1])
    if not sc in s:
        s.add(sc)

print len(list(s))