read = open('in.txt', 'r')
write = open('out.txt', 'w')

def f(x):
    a = x if x >= 11 and x <= 13 else str(x)[-1]
    return {
        1 : 'st',
        2 : 'nd',
        3 : 'rd',
    }.get(int(a), 'th')

def solve(index, final):
    a = read.readline().strip()[0:-2]
    write.write(f'{a}{f(int(a))}\n')
           
count = int(read.readline())
for i in range(0, count):
    solve(i+1, i == count-1)
