read = open('in.txt', 'r')
write = open('out.txt', 'w')

def solve(index, final):
    a = [0, 0, 0]
    w = -1
    result = 'NO WINNER'
    for i in read.readline().strip().split(' '):
        if i == 'R':
            a[0] += 1
        elif i == 'P':
            a[1] += 1
        else:
            a[2] += 1
    if min(a) == 0:
        if a.count(0) == 1:
            if a[0] == 0 and a[2] == 1:
                result = 'SCISSORS'
            elif a[1] == 0 and a[0] == 1:
                result = 'ROCK'
            elif a[2] == 0 and a[1] == 1:
                result = 'PAPER'
    write.write(f'{result}\n')
           



count = int(read.readline())
for i in range(0, count):
    solve(i+1, i == count-1)


read.close()
write.close()