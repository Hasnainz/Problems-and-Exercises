read = open('in.txt', 'r')
write = open('out.txt', 'w')

def gradient(x1,y1,x2,y2):
    return 'vertical' if x2 - x1 == 0 else (y2-y1)/(x2-x1)

def c(m, x, y):
    return 'undefined' if m == 'vertical' else (y - (m*x))

def xyint(m1, c1, m2, c2, x1, x2):
    if m1 == m2: return ['YES' 'YES']
    if m1 == 'vertical': return [x1,m2*x1+c2]
    elif m2 == 'vertical': return [x2,m1*x2+c2]
    else: return [(c2-c1)/(m1-m2), (c1*m2-c2*m1)/(m2-m1)]


def solve(index, final):
    sx, sy, cx, cy, w = [int(x) for x in [read.readline().strip().split(' ')][0]]
    scm = gradient(sx, sy, cx, cy)
    scc = c(scm, sx, sy)
    r = 0
    for i in range(int(w)):
        x, y, ex, ey = [int(x) for x in [read.readline().strip().split(' ')][0]]
        wm = gradient(x,y,ex,ey)
        wc = c(wm,x,y)
        xint, yint = xyint(wm, wc, scm, scc, x, sx)
        if xint != 'YES':
            a = [sx, cx, x, ex]
            b = [sy, cy, y, ey]
            if xint >= min(a) and xint <= max(a) and yint >= min(b) and yint <= max(b):
                r += 1
                break
    if r >= 1: write.write('NO\n')
    else: write.write('YES\n')    




count = int(read.readline().strip())
for i in range(0, count):
    solve(i+1, i == count-1)
