import re
import time

challenge_input = open('7.txt').read().split('\n')

var = {}

for cmd in challenge_input:
    var[cmd.split(' -> ')[1]] = cmd.split(' -> ')[0].replace('NOT ', '~').replace(' AND ', '&').replace(' OR ', '|').replace(' LSHIFT ', '<<').replace(' RSHIFT ', '>>')

def eval_next(x):
    if x in ['', '&', '~', '|', '<<', '>>'] or x.isdigit():
        return x
    else:
        val = eval(''.join(map(eval_next, re.split('(&|\||>>|<<|~)', var[x]))))
        return str(val) if val > 0 else str(65536 + val)

print eval_next('d')
print eval_next('e')
print eval_next('f')
print eval_next('g')
print eval_next('h')
print eval_next('i')
print eval_next('x')
print eval_next('y')
