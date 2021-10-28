read = open('in.txt', 'r')
write = open('out.txt', 'w')

def f(x1,x2,y1,y2,z1,z2): 
    return (((x2-x1)**2)+((y2-y1)**2)+((z2-z1)**2)) ** (0.5)


def solve(index, final):
    Cr,Cg,Cb,T,Fr,Fg,Fb,Br,Bg,Bb = [int(x) for x in read.readline().strip().split(' ')]
    a = f(Fr,Cr,Fg,Cg,Fb,Cb)
    if a <= float(T): write.write(f'{Br} {Bg} {Bb}\n')
    else: write.write(f'{Fr} {Fg} {Fb}\n')

count = int(read.readline().strip())
for i in range(0, count):
    solve(i+1, i == count-1)

read.close()
write.close()