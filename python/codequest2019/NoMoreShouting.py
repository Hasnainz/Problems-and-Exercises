file1 = open("out.txt","w") 
 
def solve():
    line = input('')
    file1.write(line.lower() + '\n')
    

count = int(input(''))
for i in range(0, count):
    solve()

file1.close()
