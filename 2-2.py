a = open('2.txt').read().split('\n')

total = 0

for x in a:
    x = map(int, x.split('x'))
    total += 2*sum(sorted(x)[:2])
    total += reduce(lambda x, y: x*y, x)

print total