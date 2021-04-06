read = open('in.txt', 'r')
write = open('out.txt', 'w')

#Using a dictionary for faster lookup times
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
    }.get(c.lower(), '???') 

def solve(index, final):
    word = read.readline().strip()
    r = ''
    for c in word:
        print(f'c : {c}')
        is_upper = c.isupper()
        a = f(c)
        print(f'a : {a}')
        if a <= 5: a += 6
        elif a <= 10: a = a ** 2
        elif a <= 15: a = (a % 3) * 5 + 1
        elif a <= 20: a = sum([int(x) for x in str(a)]) * 8
        else:
            q = a - 1
            while a % q != 0:
                q -= 1
            a = q * 2
        while a > 26: a -= 26
        print(f'a : {a}')
        if a == 0: r += c
        else: r += g(a).upper() if is_upper else g(a)
    write.write(f'{r}\n')



count = int(read.readline().strip())
for i in range(0, count):
    solve(i+1, i == count-1)

read.close()
write.close()