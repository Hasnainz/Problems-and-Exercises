import sys
import math
from datetime import timedelta

def reg_round(n, dp):
    import math
    n *= 10 ** dp
    if n - math.floor(n) < 0.5: 
        return math.floor(n)/10 ** dp
    return math.ceil(n)/10 ** dp

def solve(index, last):
    d, v = [float(x) for x in sys.stdin.readline().strip().split()]
    days = ((d*1000000)/v)/24
    hours = (days-math.floor(days))*24
    mins = (hours-math.floor(hours)) * 60
    secs = (mins-math.floor(mins)) * 60 
    print(f'Time to Mars: {math.floor(days)} days, {math.floor(hours)} hours, {math.floor(mins)} minutes, {int(reg_round(secs,0))} seconds')


count = int(sys.stdin.readline().strip())
for i in range(0, count):
    solve(i+1, i == count-1)



