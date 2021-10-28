import sys

read = open('out.txt', 'r')
run_test = True if '-t' in sys.argv else False
    

def solve(index, final):
    a,b,c = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    t = f'${(a*31*0.05 + b*15*0.1 + c*0.5*0.2):.2f}'

    
    if run_test:
        output_line = read.readline().strip()
        if output_line != t:
            print(f"Outputs don't match:\nWhat you got: {t}\nWhat they got: {output_line}")
    else: print(t)

count = int(sys.stdin.readline().strip())
for i in range(count):
    solve(i+1, i == count-1)

read.close()
