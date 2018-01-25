a = open('1.txt').read()

print sum([-1 if x == ')' else 1 for x in a])