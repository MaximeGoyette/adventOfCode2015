import re
import itertools

data = open('13.txt').read()

data = {(a, b): {'gain': 1, 'lose': -1}[s]*int(n) for a, s, n, b in re.findall(r'(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).', data)}
persons = set()
for a, b in data:
    persons.add(a)
    persons.add(b)

max_score = None

def get_score(c):
    score = 0
    for a, b in [(c[i - 1], c[i]) for i in xrange(len(c))]:
        score += data[(a, b)] + data[(b, a)]
    return score

for configuration in itertools.permutations(persons):
    score = get_score(configuration)
    if max_score == None or score > max_score:
        max_score = score

print max_score
