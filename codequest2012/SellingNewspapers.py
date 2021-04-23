import sys

t = 0
lines = [x.strip() for x in sys.stdin.readlines()]
for line in lines:
    a, b = [int(x) for x in line.split(' ')]
    c = a-b
    if c == 0:print('Times and Herald have the same number of subscribers')
    elif c < 0:print(f'Herold has {abs(c)} more subscribers')
    else: print(f'Times has {c} more subscribers')