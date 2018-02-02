from itertools import groupby

a = open('10.txt').read()

for _ in xrange(50):
    a = ''.join([str(sum(1 for _ in g)) + k for k, g in groupby(a)])

print len(a)