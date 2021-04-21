import sys

def solve(index, final):
    x, d, e = sys.stdin.readline().strip().split()
    for i in range(int(x)):
        r = ''
        a = sys.stdin.readline().strip()
        c = 0
        f = 1
        if a != '':
            while c < len(a):
                if a[c] == e:
                    c += 1
                    r += a[c]
                elif a[c] == '"':
                    c += 1
                    while c < len(a) and a[c] != '"':
                        if a[c] == e:
                            c += 1
                            r += a[c]
                            c += 1
                        else: 
                            r += a[c]
                            c += 1
                elif a[c] == d:
                    if r == '': r = '<BLANK>'
                    print(f'Record {i+1}, Field {f}: {r}')
                    r = ''
                    f += 1
                else:
                    r += a[c]
                if c == len(a) - 1:
                    if r == '': r = '<BLANK>'
                    print(f'Record {i+1}, Field {f}: {r}')
                    break
                c += 1
        else: 
            print(f'Record {i+1}, Field {f}: <BLANK>')
            f += 1

count = int(sys.stdin.readline().strip())
for i in range(count):
    solve(i+1, i == count-1)
