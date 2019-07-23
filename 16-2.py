import re

data = open('16.txt').read().split('\n')
data = [{x:int(y) for x, y in re.findall(r'(\w+): (\d+)', line)} for line in data]

target = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

for i, line in enumerate(data):
    if 'children' in line and line['children'] != target['children']:
        continue
    if 'cats' in line and line['cats'] <= target['cats']:
        continue
    if 'samoyeds' in line and line['samoyeds'] != target['samoyeds']:
        continue
    if 'pomeranians' in line and line['pomeranians'] >= target['pomeranians']:
        continue
    if 'akitas' in line and line['akitas'] != target['akitas']:
        continue
    if 'vizslas' in line and line['vizslas'] != target['vizslas']:
        continue
    if 'goldfish' in line and line['goldfish'] >= target['goldfish']:
        continue
    if 'trees' in line and line['trees'] <= target['trees']:
        continue
    if 'cars' in line and line['cars'] != target['cars']:
        continue
    if 'perfumes' in line and line['perfumes'] != target['perfumes']:
        continue

    print i + 1
