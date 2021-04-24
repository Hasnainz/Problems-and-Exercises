#Rounds 5 up instead of down like the round() function
#Doesn't lose any accuracy (in theory)
def reg_round(n, dp):
    import math
    n *= 10 ** dp
    if n - math.floor(n) < 0.5: 
        return math.floor(n)/10 ** dp
    return math.ceil(n)/10 ** dp

#Calculates the distance between 3 points in 3d space
def distance_3D(x1,x2,y1,y2,z1,z2): 
    return (((x2-x1)**2)+((y2-y1)**2)+((z2-z1)**2)) ** (0.5)

#Calculates the distance between 2 points in 2d space
def distance_2D(x1,x2,y1,y2): 
    return (((x2-x1)**2)+((y2-y1)**2)) ** (0.5)

#Using a dictionary for faster lookup times

def letter_to_number(c): 
    return ord(c.lower()) - ord('a') + 1 if c.isalpha() else '???'

def number_to_letter(n):
    return chr(n+ord('a')-1)


read = open('in.txt', 'r')
write = open('out.txt', 'w')

def solve(index, final):
    pass

count = int(read.readline().strip())
for i in range(0, count):
    solve(i+1, i == count-1)

read.close()
write.close()

#Comparing 2 files line by line
f1 = open('my_out.txt', 'r')
f2 = open('out.txt', 'r')

l1 = f1.readlines()
l2 = f2.readlines()

for i,v in enumerate(l1):
    if v != l2[i]:
        print(f'line number: {i+1}, {v.strip()} {l2[i].strip()}')

f1.close()                                       
f2.close()                                      

#Fastest way to remove duplicates
list(dict.fromkeys(items))

def readline():
    import sys
    return sys.stdin.readline().strip()