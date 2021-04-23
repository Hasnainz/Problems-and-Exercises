import sys

lines = [x.strip() for x in sys.stdin.readlines()]
for line in lines:
    try: 
        a = [int(x) for x in line.split(' ')]
    except: 
        print('The input was invalid')
        break
    if a == sorted(a): print('The numbers are in ascending order')
    elif a == sorted(a, reverse=True): print('The numbers are in descending order')
    else: print('The numbers are in random order')