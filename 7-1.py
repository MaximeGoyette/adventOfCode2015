import re
import traceback

lines = '''123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i'''.replace('\r', '').split('\n')
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

while lines:
    print(len(lines))
    line = lines.pop(0)
    try:
        for op, f in ops.iteritems():
            m = re.match(op, line)
            if m:
                args, target = m.groups()[:-1], m.groups()[-1]
                args = [wires.get(a) or int(a) for a in args]
                wires[target] = f(*args)
                break
    except:
        traceback.print_exc()
        lines.append(line)

print wires