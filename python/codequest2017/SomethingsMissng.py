import sys

def solve(index, last):
    a, b = sys.stdin.readline().strip().split()
    print(''.join([v for i, v in enumerate(a) if i != int(b)]))

count = int(sys.stdin.readline().strip())
for i in range(0, count):
    solve(i+1, i == count-1)