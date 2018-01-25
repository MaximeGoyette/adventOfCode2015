import md5

k = 'ckczppom'

i = 1
while True:
    h = md5.new(k + str(i)).hexdigest()
    if h[:6] == '0'*6:
        print i
        exit()
    i += 1