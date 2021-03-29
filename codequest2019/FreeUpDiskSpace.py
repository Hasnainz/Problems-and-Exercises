import datetime
read = open('in.txt', 'r')
write = open('out.txt', 'w')


def reg_round(n, dp):
    import math
    n *= 10 ** dp
    if n - math.floor(n) < 0.5:
        return math.floor(n)/10 ** dp
    return math.ceil(n)/10 ** dp


today = datetime.date(2019, 4, 27)

def score(d,t,m,s):
    a,b,c = [int(x) for x in d.split('/')] 
    dif = today - datetime.date(c, b, a)
    days = float(dif.days)
    if m == 'PM': days -= 0.5
    else: days -= 0.5
    print(days)
    print(s)
    return days * s


def solve(index, final):
    f, c = [read.readline().strip().split(' ')][0]
    f = int(f)
    c = float(c)
    r = [None]*f
    result = []
    c = (c * 1000)/4
    total = 0
    point = 0
    for i in range(f):
        d, t, m, s, n = [read.readline().strip().split(' ')][0]
        s = int(s)/1000
        r[i] = [score(d,t,m,s), n, s]
    r.sort(key=lambda x: x[0], reverse=True)
    print(r)
    while total < c:
        spret = reg_round(r[point][0], 3)
        write.write(f'{r[point][1]} {spret:.3f}\n')
        total += r[point][2]
        result.append(r[point][2])
        point += 1
              

count = int(read.readline().strip())
for i in range(0, count):
    solve(i+1, i == count-1)
