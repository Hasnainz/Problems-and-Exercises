file1 = open("out.txt","w") 

def solve():
    line = (input(''))
    a,b,c = [ int(x) for x in line.split(" ")]
    doors = []
    for i in range(0, a):
        doors.append(float(100.0)/float(a))
    for i in range(1, b+1):
        for j in range(0, c):
            doors.pop()
        new_chance = float(100)
        for j in range(0, i):
            new_chance -= doors[j]
        new_chance /= float((len(doors) - i))
        for j in range(i, len(doors)):
            doors[j] = new_chance
    file1.write(f'{max(doors):.2f}%\n')

count = int(input(''))
for i in range(0, count):
    solve()
    
    

file1.close()

