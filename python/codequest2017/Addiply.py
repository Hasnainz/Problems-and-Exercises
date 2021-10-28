import sys

def solve(index, last):
    a, b = [int(x) for x in sys.stdin.readline().strip().split()]
    print(f'{a+b} {a*b}')

count = int(sys.stdin.readline().strip())
for i in range(0, count):
    solve(i+1, i == count-1)