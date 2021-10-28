read = open('in.txt', 'r')
write = open('out.txt', 'w')

def solve(index, final):
    if int(read.readline().strip()) >= 70:
        write.write('PASS\n')
    else:
        write.write('FAIL\n')



count = int(read.readline())
for i in range(0, count):
    solve(i+1, i == count-1)

read.close()
write.close()