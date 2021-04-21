import sys

read = open('out.txt', 'r')
run_test = True if '-t' in sys.argv else False
    
def reg_round(n, dp):
    import math
    n *= 10 ** dp
    if n - math.floor(n) < 0.5: 
        return math.floor(n)/10 ** dp
    return math.ceil(n)/10 ** dp

def solve(index, final):
    gears = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    t = 1
    for i in range(1, len(gears)):
        t *= gears[i]/gears[i-1]
    t = f'{reg_round(t, 2):.2f}:1'
    if run_test:
        output_line = read.readline().strip()
        if output_line != t:
            print(f"Outputs don't match:\nWhat you got: {t}\nWhat they got: {output_line}")
    else: print(t)

count = int(sys.stdin.readline().strip())
for i in range(count):
    solve(i+1, i == count-1)

read.close()
