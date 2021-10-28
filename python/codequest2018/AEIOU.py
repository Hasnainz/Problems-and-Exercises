read = open('in.txt', 'r')
write = open('out.txt', 'w')

def solve(index, final):
    a = read.readline().strip().lower()
    b = a.count('a') + a.count('e') + a.count('i') + a.count('o') + a.count('u')
    write.write(f'{b}\n')

count = int(read.readline().strip())
for i in range(0, count):
    solve(i+1, i == count-1)

read.close()
write.close()