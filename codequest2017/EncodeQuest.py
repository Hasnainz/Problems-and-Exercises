import sys

def f(c):
    return {
        'a' : 1, 'n' : 14,
        'b' : 2, 'o' : 15,
        'c' : 3, 'p' : 16,
        'd' : 4, 'q' : 17,
        'e' : 5, 'r' : 18,
        'f' : 6, 's' : 19,
        'g' : 7, 't' : 20,
        'h' : 8, 'u' : 21,
        'i' : 9, 'v' : 22,
        'j' : 10, 'w' : 23,
        'k' : 11, 'x' : 24,
        'l' : 12, 'y' : 25,
        'm' : 13, 'z' : 26
    }.get(c, '???') 

def g(n):
    return {
        1 : 'a', 14 : 'n',
        2 : 'b', 15 : 'o',
        3 : 'c', 16 : 'p',
        4 : 'd', 17 : 'q',
        5 : 'e', 18 : 'r',
        6 : 'f', 19 : 's',
        7 : 'g', 20 : 't',
        8 : 'h', 21 : 'u',
        9 : 'i', 22 : 'v',
        10 : 'j', 23 : 'w',
        11 : 'k', 24 : 'x',
        12 : 'l', 25 : 'y',
        13 : 'm', 26 : 'z'
    }.get(n, '???') 

def solve(index, last):
    t = sys.stdin.readline().strip().lower()
    k = sys.stdin.readline().strip().lower()
    while len(k) <= len(t):
        k += k
    r = ''
    s = 0
    for i, c in enumerate(t):
        if c.isalpha():
            a = f(c) + f(k[i + s]) - 1
            while a > 26: a -= 26
            r += g(a)
        else: 
            r += ' '
            s -= 1

    print(r.upper())


count = int(sys.stdin.readline().strip())
for i in range(0, count):
    solve(i+1, i == count-1)