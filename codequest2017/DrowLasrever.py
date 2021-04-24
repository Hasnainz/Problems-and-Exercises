import sys
import string
import re

def solve(index, last):
    b = sys.stdin.readline().strip()
    a = b.split()
    a = [re.split("[!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]", x) for x in a]
    a = [[y[::-1] for y in x] for x in a]
    a = ' '.join(['.'.join(x) for x in a])
    r = ''
    for i in range(len(a)):
        if a[i].isalpha(): r += a[i]
        else: r += b[i]
    print(r)


count = int(sys.stdin.readline().strip())
for i in range(0, count):
    solve(i+1, i == count-1)