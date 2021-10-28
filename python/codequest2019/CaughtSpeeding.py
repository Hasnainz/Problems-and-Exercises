file1 = open("out.txt","w") 
 
def solve():
    line = input('')
    a,b = [ str(x) for x in line.split(" ")]
    a = int(a)
    b = True if b == "true" else False
    #print(f'\na:{str(a)}, b:{str(b)}\n')
    if b:
        a -= 5
    if a <= 60:
        file1.write(f'no ticket\n')
    elif a <= 80:
        file1.write(f'small ticket\n')
    else:
        file1.write(f'big ticket\n')

count = int(input(''))
for i in range(0, count):
    solve()

file1.close()
