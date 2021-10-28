read = open('in.txt', 'r')
write = open('out.txt', 'w')

def solve(index, final):
    n = int(read.readline().strip())
    o = n
    i = 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n*3 + 1
        i += 1
    write.write(f'{o}:{i}\n')

count = int(read.readline().strip())
for i in range(0, count):
    solve(i+1, i == count-1)

read.close()
write.close()