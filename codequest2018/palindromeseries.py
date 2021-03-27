read = open('in.txt', 'r')
write = open('out.txt', 'w')

def solve(index, final):
    r = int(read.readline().replace('\n', ''))
    c = [0] * r
    result = ''
    for i in range(1, r+1):
        a = (str(read.readline())).strip().lower()
        if a[::-1] != a:
            c[i-1] = 1
    if max(c) != 0:
        result = 'False - ' + ', '.join([str(i+1) for i, x in enumerate(c) if x != 0])
    else:
        result = 'True'
    write.write(f'{result}\n')



count = int(read.readline())
for i in range(0, count):
    solve(i+1, i == count-1)
