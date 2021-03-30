read = open('in.txt', 'r')
write = open('out.txt', 'w')

'''
1) Split arrays into arrays split by zeros
2) Subtract all numbers in array by min
3) Add that min to the total
4) Repeat on that split array, return to one until
    the maximum value of the array is empty
'''
    

def solve(index, final):
    n = int(read.readline())
    f = [int(x) for x in read.readline().split()]
    result = f'Case #{index}: '
    t = 0
    while max(f) != 0:
        l = 0
        if f[l] == 0:
            while l < n and f[l] == 0:
                l += 1
        r = l
        while r < n and f[r] != 0:
            r += 1
        low = min(f[l:r])
        for i in range(l, r):
            f[i] -= low
        t += low

    result += f'{t}\n'
    print(result)
    write.write(result)


count = int(read.readline())
for i in range(0, count):
    solve(i+1, i == count-1)

read.close()
write.close()