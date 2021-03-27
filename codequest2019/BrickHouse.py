file1 = open("out.txt","w") 
 
def solve():
    line = input('')
    a,b,c = [ int(x) for x in line.split(" ")]
    total = a + (5*b)
    if total >= c:
        file1.write(f'true\n')
    else:
        file1.write(f'false\n')
        
count = int(input(''))
for i in range(0, count):
    solve()

file1.close()
