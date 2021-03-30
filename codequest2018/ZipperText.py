read = open('in.txt', 'r')
write = open('out.txt', 'w')
    

#Splits a string
def split_lines(s, a):
    r = ''
    for i in range(1, len(a)): a[i] += a[i-1]
    a = [0] + a + [len(s)]
    for i in range(0, len(a)-1):
        r += s[a[i]:a[i+1]]
        r += '\n'
    return r.rstrip()

def solve(index, final):
    nu = int(read.readline().strip())
    u = [int(x) for x in read.readline().strip().split(' ')]
    nl = int(read.readline().strip())
    l = [int(x) for x in read.readline().strip().split(' ')]
    m = ''.join([x.strip() for x in read.readlines()])
    ru = ''
    rl = ''
    for c in m:
        if c.isupper(): ru += c
        else:
            if c == '-': ru += ' '
            elif c == '=': rl += ' '
            else: rl += c
    ru = split_lines(ru, u)
    rl = split_lines(rl, l)
    write.write(f'{ru}\n\n{rl}')

count = int(read.readline().strip())
for i in range(0, count):
    solve(i+1, i == count-1)

read.close()
write.close()