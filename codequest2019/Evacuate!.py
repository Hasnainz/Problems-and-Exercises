read = open('in.txt', 'r')
write = open('out.txt', 'w')

def check_completed(r, end):
    for p in end:
        a, b = p
        if r[a][b] == 0:
            return False
    return True

def increment_max(r, c):
    for i in range(len(r)):
        for j in range(len(r[i])):
            if r[i][j] == c:
                if j-1 >= 0 and r[i][j-1] == 0: r[i][j-1] = c+1
                if j+1 < len(r[i]) and r[i][j+1] == 0: r[i][j+1] = c+1
                if i-1 >= 0 and r[i-1][j] == 0: r[i-1][j] = c + 1
                if i+1 < len(r) and r[i+1][j] == 0: r[i+1][j] = c+1
    
def read_map(w, h):
    r = []
    o = []
    start = [0, 0]
    end = []
    for i in range(h):
        q = read.readline().strip()
        o.append(q)
        temp = []
        for c in q: 
            if c == 'o':
                start = [i, q.index('o')]
                temp.append(1)
            elif c == 'X':
                end.append([i, q.index('X')])
                temp.append(0)
            elif c == '#': temp.append('#')
            else: temp.append(0)
        r.append(temp)
    current_distance = 1
    while not check_completed(r, end):
        increment_max(r, current_distance)
        current_distance += 1
    return r, start, end, o



def draw_shortest_path(s_x, s_y, e_x, e_y, r, w ):
    k = r[e_x][e_y]
    while k > 1:
        if e_x-1 >= 0 and r[e_x-1][e_y] == k-1:
            e_x, e_y = e_x-1, e_y
            k -= 1
        elif e_y-1 >= 0 and r[e_x][e_y-1] == k-1:
            e_x, e_y = e_x, e_y-1
            k -= 1
        elif e_x+1 < len(r) and r[e_x+1][e_y] == k-1:
            e_x, e_y = e_x+1, e_y
            k -= 1
        elif e_y+1 < len(r[e_x]) and r[e_x][e_y+1] == k-1:
            e_x, e_y = e_x, e_y+1
            k -= 1
        w[e_x] = w[e_x][:e_y] + '.' + w[e_x][e_y+1:]

def solve(index, final):
    width, height = [int(x) for x in read.readline().strip().split(' ')]
    routes, start, ends, w = read_map(width, height)
    finals = []
    for end in ends:
        a = [routes[end[0]][end[1]], end[0], end[1]]
        finals.append(a)
    s_dist = min(finals, key=lambda x: x[0])
    draw_shortest_path(start[0], start[1], a[1], a[2], routes, w)
    w[start[0]] = w[start[0]][:start[1]] + 'o' + w[start[0]][start[1]+1:]
    for line in w:
        write.write(f'{line}\n')


count = int(read.readline().strip())
for i in range(0, count):
    solve(i+1, i == count-1)

read.close()
write.close()