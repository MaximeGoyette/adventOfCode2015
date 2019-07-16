import re

data = open('12.txt').read()

numbers = re.findall(r'(-?\d+)', data)

print sum(map(int, numbers))
