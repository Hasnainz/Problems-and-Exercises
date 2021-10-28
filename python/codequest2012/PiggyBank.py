import sys

t = 0
lines = [x.strip() for x in sys.stdin.readlines()]
for line in lines:
    c, n = line.split('=')
    n = int(n)
    if c == 'PENNY': t += n
    elif c == 'NICKEL': t += n*5
    elif c == 'DIME': t += n*10
    elif c == 'QUARTER': t += n*25
    elif c == 'HALFDOLLAR': t += n*50

print(f'${t/100:.2f}')
