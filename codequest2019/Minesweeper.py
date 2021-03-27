file1 = open("out.txt","w") 

def solve():
    line = (input(''))
    row,col,bom = [ int(x) for x in line.split(" ")]
    bomb_loc = []
    for i in range(0, bom):
        l = (input(''))
        bomb_loc.append([ int(x) for x in l.split(" ")])
    
    grid = []
    for i in range(0, row):
        temp = []
        for j in range(0, col):
            temp.append(0)
        grid.append(temp)
    for bomb in bomb_loc:
        a = bomb[0]
        b = bomb[1]
        grid[a][b] = '*'
        for i in range(a-1, a+2):
            for j in range(b-1, b+2):
                if i >= 0 and i < row and j >= 0 and j < col:
                    if grid[i][j] != '*':
                        grid[i][j] += 1
    file1.write('\n'.join(''.join(str(x) for x in row) for row in grid))
    file1.write('\n')


count = int(input(''))
for i in range(0, count):
    solve()
    
    

file1.close()

