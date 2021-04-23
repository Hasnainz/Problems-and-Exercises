import sys

def solve(index, last):
    a = sys.stdin.readline().strip()[::-1]
    print(a)

count = int(sys.stdin.readline().strip())
for i in range(0, count):
    solve(i+1, i == count-1)