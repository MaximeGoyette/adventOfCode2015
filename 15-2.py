import re

data = open('15.txt').read()
data = re.findall(r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)', data)
data = [(a, int(b), int(c), int(d), int(e), int(f)) for a, b, c, d, e, f in data]

max_score = None

for a in xrange(1, 98):
    for b in xrange(1, 98):
        for c in xrange(1, 98):
            d = 100 - a - b - c
            if d >= 1:
                capacity   = max(0, a*data[0][1] + b*data[1][1] + c*data[2][1] + d*data[3][1])
                durability = max(0, a*data[0][2] + b*data[1][2] + c*data[2][2] + d*data[3][2])
                flavor     = max(0, a*data[0][3] + b*data[1][3] + c*data[2][3] + d*data[3][3])
                texture    = max(0, a*data[0][4] + b*data[1][4] + c*data[2][4] + d*data[3][4])
                calories   = a*data[0][5] + b*data[1][5] + c*data[2][5] + d*data[3][5]
            if calories != 500:
                continue
            score = capacity*durability*flavor*texture
            if score > max_score:
                max_score = score
        
print max_score
