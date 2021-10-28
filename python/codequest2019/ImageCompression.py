import math
file1 = open("out.txt","w") 
 
def solve():
    newcount = int(input(''))
    val_list = []
    for i in range(0, newcount):
        val_list.append(float(input('')))
    for item in val_list:
        output = round(((item - min(val_list))/(max(val_list) - min(val_list)))*255,0)
        file1.write(f'{int(output)}\n')

        
count = int(input(''))
for i in range(0, count):
    solve()

file1.close()
