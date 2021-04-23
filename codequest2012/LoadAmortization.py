import sys

lines = [x.strip() for x in sys.stdin.readlines()]
for i in range(0, len(lines)):
    p, y, t, m = lines[i].split(' ')
    p = float(p)
    j = float(y) / 1200
    n = int(t)
    m = int(m)
    a = p * j / (1-(1+j)**-n)
    for i in range(m): p = p - (a - (p * j))
    print(f'{p:.2f}')