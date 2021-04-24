import sys

def reg_round(n, dp):
    import math
    n *= 10 ** dp
    if n - math.floor(n) < 0.5: 
        return math.floor(n)/10 ** dp
    return math.ceil(n)/10 ** dp

def solve(index, last):
    n = int(sys.stdin.readline().strip())
    a = 0
    t = 0.0
    for i in range(n):
        d, pur, pay = sys.stdin.readline().strip().split(',') 
        try: t += float(pur)
        except: pass
        try: t -= float(pay)
        except: pass
        a += t
    m = (a/n)*(0.18)/12
    print(f'${reg_round(m, 2):.2f}')

count = int(sys.stdin.readline().strip())
for i in range(0, count):
    solve(i+1, i == count-1)