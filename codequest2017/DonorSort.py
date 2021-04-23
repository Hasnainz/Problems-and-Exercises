import sys


def solve(index, last):
    a = sys.stdin.readline().strip().split(',')
    b = sys.stdin.readline().strip().split(',')
    c = a + b
    print(','.join([x for x in sorted(a) if x not in b]))
    print(','.join(list(dict.fromkeys([x for x in sorted(c) if c.count(x) > 1]))))
    print(','.join([x for x in sorted(b) if x not in a]))

count = int(sys.stdin.readline().strip())
for i in range(0, count):
    solve(i+1, i == count-1)



