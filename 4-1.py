import md5

k = 'ckczppom'

i = 1
while True:
    h = md5.new(k + str(i)).hexdigest()
    if h[:5] == '0'*5:
        print i
        exit()
    i += 1