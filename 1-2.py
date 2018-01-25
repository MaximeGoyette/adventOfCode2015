a = open('1.txt').read()

n = 0

for i in range(len(a)):
    if a[i] == '(':
        n += 1
    else:
        n -= 1
    if n < 0:
        print i
        exit()
    i += 1
