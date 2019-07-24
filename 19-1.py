import re
data = open('19.txt').read()

replacements = re.findall(r'(\w+) => (\w+)', data)
molecule = data.split('\n')[-1]

results = set()

for a, b in replacements:
    indices = [m.start() for m in re.finditer(a, molecule)]
    for i in indices:
        results.add(molecule[:i] + b + molecule[i + len(a):])

print len(results)
