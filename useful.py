def reg_round(n, dp):
    import math
    n *= 10 ** dp
    if n - math.floor(n) < 0.5:
        return math.floor(n)/10 ** dp
    return math.ceil(n)/10 ** dp


read = open('in.txt', 'r')
write = open('out.txt', 'w')

def solve(index, final):
    pass

count = int(read.readline().strip())
for i in range(0, count):
    solve(i+1, i == count-1)

read.close()
write.close()