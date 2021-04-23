import sys

def solve(index, last):
    a = sorted([int(x) for x in sys.stdin.readline().strip().split(',')])
    print(','.join([str(x) for x in a]))

count = int(sys.stdin.readline().strip())
for i in range(0, count):
    solve(i+1, i == count-1)