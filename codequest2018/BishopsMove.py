read = open('in.txt', 'r')
write = open('out.txt', 'w')

def is_even(x):
    return True if x % 2 == 0 else False 

def solve(index, final):
    r, c = [int(x) for x in read.readline().split(',')]
    r1, c1 = [int(x) for x in read.readline().split(',')]
    r2, c2 = [int(x) for x in read.readline().split(',')]
    a = is_even(r1-c1)
    b = is_even(r2-c2)
    if a == b:
        write.write('Yes\n')
    else:
        write.write('No\n')

count = int(read.readline())
for i in range(0, count):
    solve(i+1, i == count-1)

read.close()
write.close()