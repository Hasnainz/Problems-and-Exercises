read = open('in.txt', 'r')
write = open('out.txt', 'w')


#TODO: If this puzzle has a larger input size
#its not practical to loop throught the array
#just remove using a range loop instead of checking
#values because we know which exact values should be 
#eliminated.

def solve(index, final):
    a = int(read.readline().strip())
    b = list(range(2, a+1))
    r = []
    while len(b) > 0:
        r.append(b[0])
        i = 0
        c = 0
        p = b[0]
        while i < len(b):
            if b[i] % p == 0:
                b.remove(b[i])
                c += 1
            i += 1
        if c >= 2:
            write.write(f'Prime {p} Composite Set Size: {c-1}\n')
    write.write('{' + f"{','.join([str(x) for x in r])}" + '}\n')


count = int(read.readline().strip())
for i in range(0, count):
    solve(i+1, i == count-1)


read.close()
write.close()