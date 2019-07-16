import json

data = json.load(open('12.txt'))

def get_total(a):
    total = 0
    if isinstance(a, int):
        return a
    elif isinstance(a, list):
        for x in a:
            total += get_total(x)
        return total
    elif isinstance(a, dict):
        if not any(['red' in (x, y) for x, y in a.iteritems()]):
            for x, y in a.iteritems():
                total += get_total(y)
    return total

print get_total(data)
