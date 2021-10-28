file1 = open("out.txt","w") 


def getVal(word):
    a = 0
    for char in word:
        a += ord(char) - 96
    return a

def solve():
    data_values = input('').split(' ')
    line = input ('')
    timestamps = [ int(x) for x in line.split(' ')]
    h = 0
    for n in range(1, 11):
        h = (timestamps[n-1] + getVal(data_values[n-1]) + n + h)*50/147
    file1.write(f'{int(round(h,0))}\n')

count = int(input(''))
for i in range(0, count):
    solve()    
    

file1.close()

