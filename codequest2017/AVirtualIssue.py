import sys

def reg_round(n, dp):
    import math
    n *= 10 ** dp
    if n - math.floor(n) < 0.5: 
        return math.floor(n)/10 ** dp
    return math.ceil(n)/10 ** dp

def f(x1,x2,y1,y2):
    return y1 + (3-x1)/(x2-x1)*(y2-y1)

target_frame = 1000/90
low_thresh = target_frame * 70/100
extrapolate_thresh = target_frame * 85/100
high_thresh = target_frame * 90/100

def solve(index, last):
    f0,f1,f2,q = [float(x) for x in sys.stdin.readline().strip().split()]
    if f2 > high_thresh: print(int(q-2))
    elif f2 > extrapolate_thresh:
        if max([f(1,2,f1,f2),f(0,2,f0,f2)]) > high_thresh:
            print(int(q-2))
    elif f0 < low_thresh and f1 < low_thresh and f2 < low_thresh:
        print(int(q+1))
    else: print(int(q))


count = int(sys.stdin.readline().strip())
for i in range(0, count):
    solve(i+1, i == count-1)