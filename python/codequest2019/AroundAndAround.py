import math
file1 = open("out.txt","w") 
 
def solve():
    #line = input('')
    #a = [int(x) for x in line.split(" ")]
    a = int(input('')) + 40075/(2*math.pi)
    b = round((math.pi)*2*a,1)
    file1.write(f'{b}\n')

        
count = int(input(''))
for i in range(0, count):
    solve()

file1.close()
