read = open('in.txt', 'r')
write = open('out.txt', 'w')

def read_grid():
    r = []
    for i in range(9):
        a = read.readline().strip()
        r.append([int(x) for x in a.replace('_', '0')])
    return r

def valid(grid, x, y, v):
    for i in range(9):
        if grid[x][i] == v and i != y: return False
    for i in range(9):
        if grid[i][y] == v and i != x: return False
    qx = y // 3
    qy = x // 3
    for i in range(qy * 3, qy * 3 + 3):
        for j in range(qx * 3, qx * 3 + 3):
            if grid[i][j] == v and (i != x and j != y): return False
    return True


def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return [i, j]
    return None

def solve_puzzle(grid):
    find = find_empty(grid)
    if find == None: return True
    else: row, col = find
    for i in range(1, 10):
        if valid(grid, row, col, i):
            grid[row][col] = i
            if solve_puzzle(grid):
                return True
            grid[row][col] = 0
    return False
        
def solve(index, final):
    grid = read_grid()
    solved = solve_puzzle(grid)
    for row in grid:
        for a in row: write.write(f'{a}')
        write.write(f'\n')

count = int(read.readline().strip())
for i in range(0, count):
    solve(i+1, i == count-1)

read.close()
write.close()