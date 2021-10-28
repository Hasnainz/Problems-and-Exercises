file1 = open("out.txt","w") 

def count_neighbours(arr, x, y, size):
    n = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i >= 0 and j >= 0 and i < size and j < size:
                if not (i == x and j == y):
                    a = arr[i][j]
                    if a == 1:
                        n += 1
    return n

def solve(final):
    generations = int(input(''))
    grid = []
    read_grid = []
    size = 10
    for i in range(0, size):
        line = input('')
        grid.append(list(map(int, line)))
        read_grid.append(list(map(int, line)))
    for i in range(0, generations):
        for j in range(0, size):
            for k in range(0, size):
                n = count_neighbours(read_grid, j, k, size)
                if read_grid[j][k] == 1:
                    if n >= 2 and n <= 3:
                        grid[j][k] = 1
                    else:
                        grid[j][k] = 0
                else:
                    if n == 3:
                        grid[j][k] = 1
        for j in range(0, size):
            for k in range(0, size):
                read_grid[j][k] = grid[j][k]
    file1.write('\n'.join(''.join(str(x) for x in row) for row in grid))        
                
count = int(input(''))
for i in range(0, count):
    solve(i == count-1)    
    
file1.close()
