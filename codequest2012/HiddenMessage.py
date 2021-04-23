import sys

lines = [x.strip() for x in sys.stdin.readlines()]
a = lines[0]
for i in range(1, len(lines)):
    b = [x.split('-') for x in lines[i].split(' ')]
    for j, v in enumerate(b):
        for k, w in enumerate(v):
            b[j][k] = a[int(w) - 1]
    print(' '.join([''.join(x) for x in b]))

    