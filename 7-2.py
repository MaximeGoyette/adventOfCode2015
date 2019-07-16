import re

lines = open('7.txt').read().replace('\r', '').split('\n')
wires = {}

ops = {
    r'^NOT (\w+) -> (\w+)$': lambda a: 65535-a,
    r'^(\w+) OR (\w+) -> (\w+)$': lambda a, b: a|b,
    r'^(\w+) AND (\w+) -> (\w+)$': lambda a, b: a&b,
    r'^(\w+) LSHIFT (\w+) -> (\w+)$': lambda a, b: a<<b,
    r'^(\w+) RSHIFT (\w+) -> (\w+)$': lambda a, b: a>>b,
    r'^(\w+) -> (\w)$': lambda a: a
}

def get_value(w, a):
    b = w.get(a)
    if b == None:
        b = int(a)
    return b

while lines:
    line = lines.pop(0)
    try:
        for op, f in ops.iteritems():
            m = re.match(op, line)
            if m:
                args, target = m.groups()[:-1], m.groups()[-1]
                args = [get_value(wires, a) for a in args]
                wires[target] = f(*args)
                if target == 'b':
                    wires[target] = 3176
                break
    except:
        lines.append(line)

print wires['a']
