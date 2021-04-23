import sys

lines = [x.strip() for x in sys.stdin.readlines()]
c = 0
p_score = int(lines[c])
c += 1
n_qs = int(100 / p_score)
a=[]
for i in range(c, c+n_qs): a.append(lines[i])
c += n_qs
for i in range(int((len(lines)-(n_qs+1))/(n_qs+1))):
    name = lines[c]
    c += 1
    t = 0
    for i in range(n_qs): 
        if lines[c+i] == a[i]: t += p_score
    c += n_qs
    print(f'{name} {t}')