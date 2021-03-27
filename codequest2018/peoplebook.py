read = open('in.txt', 'r')
write = open('out.txt', 'w')



def solve(index, final):
    r = int(read.readline().strip())
    a = [x.split(',') for x in read.readline().strip()[2:-2].split('],[')]
    for i in range(r):
        n = read.readline().strip()
        k = a[0].index(n)
        write.write(f'Name: {a[0][k]}\n'
                    f'Age: {a[1][k]}\n'
                    f'Instagram: {a[2][k]}\n'
                    f'Twitter: {a[3][k]}\n'
                    f'Phone: {a[4][k]}\n'
                    f'Email: {a[5][k]}\n')



count = int(read.readline())
for i in range(0, count):
    solve(i+1, i == count-1)
