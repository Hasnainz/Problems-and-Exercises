read = open('in.txt', 'r')
write = open('out.txt', 'w')

def pad(num, dp = 2, lz = 3):
    num = str(int(round(num * 100, 0)))
    a = [num[:dp], num[dp:]]
    a[0] = a[0].zfill(lz)
    return f'{a[0]}.{a[1]}'  

def solve(index, final):
    a = [float(x) for x in read.readline().strip().split(' ')]
    for i in range(0, 3):
        a[i] -= 180
        if a[i] <= 0:
            a[i] += 360    
    write.write(f'{pad(a[0])} {pad(a[1])} {pad(a[2])}\n')

count = int(read.readline().strip())
for i in range(0, count):
    solve(i+1, i == count-1)
