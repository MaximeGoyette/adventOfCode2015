import re

data = open('16.txt').read().split('\n')
data = [set(re.findall(r'(\w+): (\d+)', line)) for line in data]

target = set([
    ('children', '3'),
    ('cats', '7'),
    ('samoyeds', '2'),
    ('pomeranians', '3'),
    ('akitas', '0'),
    ('vizslas', '0'),
    ('goldfish', '5'),
    ('trees', '3'),
    ('cars', '2'),
    ('perfumes', '1')
])

for i, line in enumerate(data):
    if target.intersection(line) == line:
        print i + 1
