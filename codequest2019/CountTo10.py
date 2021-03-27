file1 = open("out.txt","w") 

def solve():
    bitcount = int(input(''))
    a = 0
    b = (2 ** bitcount)
    for i in range(0, b):
        c = bin(i).replace("0b","").zfill(bitcount)
        file1.write(f'{c}\n')

count = int(input(''))
for i in range(0, count):
    solve()
    

file1.close()
