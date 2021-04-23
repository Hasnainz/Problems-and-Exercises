import sys

lines = [x.strip() for x in sys.stdin.readlines()]
for line in lines:
    a = ''.join([x for x in line.lower() if x != ' '])
    if a == a[::-1]: print('yes')
    else: print('no')
