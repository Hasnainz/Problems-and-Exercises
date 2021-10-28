file1 = open("out.txt","w") 
 
def solve():
    line = input('')
    a,b = [ int(x) for x in line.split(" ")]
    if a == b:
        file1.write(f'{2*(a + b)}\n')
    else:
        file1.write(f'{a + b}\n')
    

count = int(input(''))
for i in range(0, count):
    solve()

file1.close()
