file1 = open("out.txt","w") 

def solve(final):
    line = input()
    r,i = [ float(x) for x in line.split(" ") ]
    z1 = complex(r, i)
    c = complex(r, i)
    counter = 1
    while abs(z1) < 100 and counter <= 50:
        counter += 1
        z1 = z1**2 + c
    colour = ""
    if counter <= 10:
        colour = "RED"
    elif counter <= 20:
        colour = "ORANGE"
    elif counter <= 30:
        colour = "YELLOW"
    elif counter <= 40:
        colour = "GREEN"
    elif counter <= 50:
        colour = "BLUE"
    else:
        colour = "BLACK"
    if final:
        if i >= 0:
            file1.write(f'{r}+{i}i {colour}')
        else:
            file1.write(f'{r}{i}i {colour}')
    else:
        if i >= 0:
            file1.write(f'{r}+{i}i {colour}\n')
        else:
            file1.write(f'{r}{i}i {colour}\n')
                    
count = int(input(''))
for i in range(0, count):
    solve(i == count-1)    
    
file1.close()
