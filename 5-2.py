a = open('5.txt').read().split('\n')

def is_here_twice(a):
    return any([a.count(a[i:i + 2]) > 1 and a[i - 1:i + 2] != a[i]*3 and a[i:i + 3] != a[i]*3 or a[i] == a[i+1] == a[(i+2)%len(a)] == a[(i+3)%len(a)] for i in range(len(a) - 1)])

def condition2(a):
    return any([a[i] == a[i + 2] for i in range(len(a) - 2)])

def is_nice(a):
    return is_here_twice(a) and condition2(a)

print len([x for x in a if is_nice(x)])