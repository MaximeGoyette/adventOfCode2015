print sum([len(x.replace('\\','\\\\').replace('"','\\"'))+2-len(x) for x in open('8').read().split()])