import sys

def solve(index, last):
    a = int(sys.stdin.readline().strip())
    if a % 3 == 0 and a % 7 == 0: print('LOCKHEEDMARTIN')
    elif a % 3 == 0: print('LOCKHEED')
    elif a % 7 == 0: print('MARTIN')
    else: print(a)

count = int(sys.stdin.readline().strip())
for i in range(0, count):
    solve(i+1, i == count-1)