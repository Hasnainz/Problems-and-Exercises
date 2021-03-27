read = open('in.txt', 'r')
write = open('out.txt', 'w')

def _round(a, dp):
    a = int((a * (10 ** (dp + 1))) // 1)
    r = a % 10
    if r >= 5: a += 10 - r
    else: a -= r
    a //= 10
    return f'{str(a)[:-1]}.{str(a)[-1:]}'

def solve(index, final):
    q = [read.readline().strip().split(' ')]
    a, b = q[0]
    for i in range(int(a)):
        r = [read.readline().strip().split(' ')]
        c, d = r[0]
        t = 0
        for i in range(len(b)):
            if b[i] == d[i]:
                t += 1
        q = _round(t/len(b)*100, 1)
        t = float(q)
        grade = 'F'
        if t >= 90: grade = 'A'
        elif t >= 80: grade = 'B'
        elif t >= 70: grade = 'C'
        elif t >= 60: grade = 'D'
        write.write(f'{c} {q}% {grade}\n')

count = int(read.readline().strip())
for i in range(0, count):
    solve(i+1, i == count-1)
