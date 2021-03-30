read = open('in.txt', 'r')
write = open('out.txt', 'w')

def g(x):
    return {
        0 : 'off',
        1 : 'red',
        2 : 'green',
        3 : 'blue'
    }.get(x, '???')


def solve(index, final):
    r = read.readline().strip().split(' ')
    t = 0
    for i, v in enumerate(r):
        t += 2 ** (3-i) if v == 'BROKEN' else 0
    b = t % 4
    a = t // 4
    write.write(f'{g(a)} {g(b)}\n')



count = int(read.readline())
for i in range(0, count):
    solve(i+1, i == count-1)


read.close()
write.close()