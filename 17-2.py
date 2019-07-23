import itertools
containers = map(int, open('17.txt').read().split('\n'))

total = {}

for s in xrange(1, len(containers) + 1):
    for c in itertools.combinations(containers, s):
        if sum(c) == 150:
            if not len(c) in total:
                total[len(c)] = 0
            total[len(c)] += 1

print total[min(total)]
