v = 20151125
codes = {(1, 1):v}

row = 2
max_row = 2
col = 1

def next_v(v):
    return v*252533%33554393

while row <= 2978 or col <= 3083:
    v = next_v(v)
    codes[(row, col)] = v
    col += 1
    row -= 1
    if row < 1:
        max_row += 1
        row = max_row
        col = 1

print(codes[(2978, 3083)])
