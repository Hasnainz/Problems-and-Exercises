import sys

fib = [0, 1]
for i in range(90):
    fib.append(fib[i] + fib[i+1])

def solve(index, last):
    a = int(sys.stdin.readline().strip())
    print(f'{a} = {fib[a-1]}')

count = int(sys.stdin.readline().strip())
for i in range(0, count):
    solve(i+1, i == count-1)



