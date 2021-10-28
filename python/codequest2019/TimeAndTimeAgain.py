import math
file1 = open("out.txt","w") 
 
def getNum(line, index):
    if index - 2 >= 0:
        try:
            value = int(line[index-2])
            return 2
        except:
            return 1
    return 1


def solve():
    line = input('')
    s = int(line.find('s'))
    m = int(line.find('m'))
    h = int(line.find('h'))
    secs,mins,hrs = [0,0,0]
    #print(f's:{s}, m:{m}, h:{h}')
    #print(f's:{s-getNum(line, s)}, m:{m-getNum(line, m)}, h:{h-getNum(line, h)}')
    if s != -1:
        secs = int(line[s-getNum(line, s):s])
    if m != -1:
        mins = int(line[m-getNum(line, m):m])
    if h != -1:
        hrs = int(line[h-getNum(line, h):h])
    file1.write(f'{hrs:02d}:{mins:02d}:{secs:02d}\n')

count = int(input(''))
for i in range(0, count):
    solve()
    

file1.close()
