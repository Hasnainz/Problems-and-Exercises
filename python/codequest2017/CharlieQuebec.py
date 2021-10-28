import sys

def f(c):
    return {
        'a' : 'Alpha', 'n' : 'November',
        'b' : 'Bravo', 'o' : 'Oscar',
        'c' : 'Charlie', 'p' : 'Papa',
        'd' : 'Delta', 'q' : 'Quebec',
        'e' : 'Echo', 'r' : 'Romeo',
        'f' : 'Foxtrot', 's' : 'Sierra',
        'g' : 'Golf', 't' : 'Tango',
        'h' : 'Hotel', 'u' : 'Uniform',
        'i' : 'India', 'v' : 'Victor',
        'j' : 'Juliet', 'w' : 'Whiskey',
        'k' : 'Kilo', 'x' : 'Xray',
        'l' : 'Lima', 'y' : 'Yankee',
        'm' : 'Mike', 'z' : 'Zulu'
    }.get(c.lower(), '???') 


def solve(index, last):
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        r = []
        a = sys.stdin.readline().strip().split(' ')
        for word in a:
            r.append('-'.join([f(c) for c in word]))
        print(' '.join(r))


count = int(sys.stdin.readline().strip())
for i in range(0, count):
    solve(i+1, i == count-1)



