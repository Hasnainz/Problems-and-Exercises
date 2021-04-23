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
    return (((x2-x1)**2)+((y2-y1)**2))) ** (0.5)

#Using a dictionary for faster lookup times
def letter_to_number(c):
    return {
        'a' : 1, 'n' : 14,
        'b' : 2, 'o' : 15,
        'c' : 3, 'p' : 16,
        'd' : 4, 'q' : 17,
        'e' : 5, 'r' : 18,
        'f' : 6, 's' : 19,
        'g' : 7, 't' : 20,
        'h' : 8, 'u' : 21,
        'i' : 9, 'v' : 22,
        'j' : 10, 'w' : 23,
        'k' : 11, 'x' : 24,
        'l' : 12, 'y' : 25,
        'm' : 13, 'z' : 26
    }.get(c.lower(), '???') 

def number_to_letter(n):
    return {
        1 : 'a', 14 : 'n',
        2 : 'b', 15 : 'o',
        3 : 'c', 16 : 'p',
        4 : 'd', 17 : 'q',
        5 : 'e', 18 : 'r',
        6 : 'f', 19 : 's',
        7 : 'g', 20 : 't',
        8 : 'h', 21 : 'u',
        9 : 'i', 22 : 'v',
        10 : 'j', 23 : 'w',
        11 : 'k', 24 : 'x',
        12 : 'l', 25 : 'y',
        13 : 'm', 26 : 'z'
    }.get(n, '???') 

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