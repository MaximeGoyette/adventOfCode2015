a = open('5.txt').read().split('\n')

forbidden = ['ab', 'cd', 'pq', 'xy']

def has_double(a):
    return any([a[i] == a[i + 1] for i in range(len(a) - 1)])

def has_vowels(a):
    return sum([x in 'aeiou' for x in a]) >= 3

def has_forbidden(a):
    return any([x in a for x in forbidden])

def is_nice(a):
    return has_double(a) and has_vowels(a) and not has_forbidden(a)

print sum([is_nice(x) for x in a])