from sympy import factorint

data = int(open('20.txt').read())

def get_presents(n):
    total = 0
    a = []
    for i in xrange(1, n + 1):
        if n%i==0:
            total += 10*i
            a.append(i)
    return total, a


class Node:
    def __init__(self):
        children = []