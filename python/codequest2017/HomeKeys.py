import sys

def convert(c):
    return {
        'n' : 'b',
        'b' : 'v', 'o' : 'i',
        'c' : 'x', 'p' : 'o',
        'd' : 's', 'q' : '    ',
        'e' : 'w', 'r' : 'e',
        'f' : 'd', 's' : 'a',
        'g' : 'f', 't' : 'r',
        'h' : 'g', 'u' : 'y',
        'i' : 'u', 'v' : 'c',
        'j' : 'h', 'w' : 'q',
        'k' : 'j', 'x' : 'z',
        'l' : 'k', 'y' : 't',
        'm' : 'n', ',' : 'm', 
        '.' : ',' 
    }.get(c.lower(), '???') 


def solve(index, last):
    a = int(sys.stdin.readline())
    caps = False
    for i in range(a):
        b = sys.stdin.readline().strip()
        r = ''
        for c in b:
            if c == ' ': r += c
            elif c.lower() == 'a': caps = not caps
            elif c.lower() == 'z': pass
            else:
                if caps and c.isupper(): r += convert(c)
                elif caps or c.isupper(): r += convert(c).upper()
                else: r += convert(c)
        print(r)

count = int(sys.stdin.readline().strip())
for i in range(0, count):
    solve(i+1, i == count-1)