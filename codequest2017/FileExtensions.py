import sys

r = []
c = []
def solve(index, last):
    a, b = sys.stdin.readline().strip().split('.')
    if b not in r:
        r.append(b)
        c.append(1)
    else:
        c[r.index(b)] += 1

count = int(sys.stdin.readline().strip())
for i in range(0, count):
    solve(i+1, i == count-1)

for i in range(len(r)):
    print(f'{r[i]} {c[i]}')