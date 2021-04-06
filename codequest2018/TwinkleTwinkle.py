import math
read = open('in.txt', 'r')
write = open('out.txt', 'w')

def reg_round(n, dp):
    n *= 10 ** dp
    if n - math.floor(n) < 0.5: 
        return math.floor(n)/10 ** dp
    return math.ceil(n)/10 ** dp

def solve(index, final):
    xc, yc, p, r1, r2 = [int(x) for x in read.readline().strip().split(' ')]
    r = []
    c = math.pi/p
    a = math.pi/2
    for i in range(2 * p):
        x = 0
        y = 0
        if i % 2 == 0:
            x = r1 * math.cos(a) + xc
            y = r1 * math.sin(a) + yc
        else:
            x = r2 * math.cos(a) + xc
            y = r2 * math.sin(a) + yc
        a += c
        x = reg_round(x, 2)
        y = reg_round(y, 2)
        r.append(f'{x:.2f},{y:.2f}')
    a = ' '.join(r)
    write.write(f'{a}\n')



count = int(read.readline().strip())
for i in range(0, count):
    solve(i+1, i == count-1)

read.close()
write.close()