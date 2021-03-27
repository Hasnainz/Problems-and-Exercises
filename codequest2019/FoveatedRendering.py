import math
file1 = open("out.txt","w") 
 

def solve():
    line = input('')
    a, b = [int(x) for x in line.split(" ")]
    grid = []
    for i in range(0, 20):
        temp = []
        for j in range(0, 20):
            temp.append(10)
        grid.append(temp)
    grid[a][b] = 100
    for i in range(a-2, a+3):
        for j in range(b-2, b+3):
            if i >= 0 and j >= 0 and i <= 19 and j <=19:
                if i == a-2 or i == a+2 or j == b-2 or j == b+2:
                    grid[i][j] = 25
                elif i == a-1 or i == a+1 or j == b-1 or j == b+1:
                    grid[i][j] = 50
                else:
                    grid[i][j] = 100
    file1.write('\n'.join(' '.join(str(x) for x in row) for row in grid))


count = int(input(''))
for i in range(0, count):
    solve()
    file1.write('\n')

file1.close()
