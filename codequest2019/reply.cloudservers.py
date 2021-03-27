file1 = open("out.txt","w")
read = open("in.txt","r")

def solve(case, final):
    n, p = [int(x) for x in read.readline().split(' ')]
    cp = [int(x) for x in read.readline().split(' ')]
    for x in range(1, n):
        cp[x] += cp[x-1]
    l, r, best_l, best_r = [0, 0, 0, 0]
    ex = -1
    total = cp[r]
    while(r < n):
        total = cp[r]
        if l >= 1:
            total -= cp[l-1]
        if total >= p:
            if ex > total or ex == -1:
                ex = total
                best_l = l
                best_r = r
            l += 1
        else:
            r += 1

    print(f'total:{total}')
    result = f'Case #{case}: {best_l} {best_r}'
    if final:
        file1.write(f'{result}')
    else:
        file1.write(f'{result}\n')

n = int(read.readline())
for i in range(0, n):
    solve(i+1, i == n-1)
 
    
file1.close()


