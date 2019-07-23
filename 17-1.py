import itertools
containers = map(int, open('17.txt').read().split('\n'))

total = 0

for s in xrange(1, len(containers) + 1):
    for c in itertools.combinations(containers, s):
        if sum(c) == 150:
            total += 1

print total
