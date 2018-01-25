a = open('3.txt').read()

d = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}

sc = (0, 0)

s = set([sc])

for i in range(0, len(a), 2):
    sc = (sc[0] + d[a[i]][0], sc[1] + d[a[i]][1])
    if not sc in s:
        s.add(sc)

sc = (0, 0)

for i in range(1, len(a), 2):
    sc = (sc[0] + d[a[i]][0], sc[1] + d[a[i]][1])
    if not sc in s:
        s.add(sc)

print len(list(s))