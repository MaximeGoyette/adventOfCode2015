from itertools import combinations

a = open('2.txt').read().split('\n')

total = 0

for x in a:
    x = map(lambda n: n[0]*n[1], (combinations(map(int, x.split('x')), 2)))
    total += sum(map(lambda n: n*2, x)) + min(x)

print total