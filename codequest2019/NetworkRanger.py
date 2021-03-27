import ipaddress

file1 = open("out.txt","w") 

def solve(final):
    n = int(input(''))
    ips = []
    for i in range(0, n):
        ip = ipaddress.ip_address(input(''))
        ips.append(ip)

    lowest = str(min(ips)).split('.')
    highest = str(max(ips)).split('.')
    start = f'{int(lowest[0]):08b}.{int(lowest[1]):08b}.{int(lowest[2]):08b}.{int(lowest[3]):08b}'
    end = f'{int(highest[0]):08b}.{int(highest[1]):08b}.{int(highest[2]):08b}.{int(highest[3]):08b}'
    
    counter = 0
    dotseen = 0
    cidrange = ''
    while start[counter] == end[counter]:
        if start[counter] != '.':
            cidrange += start[counter]
        else:
            dotseen += 1
        counter += 1
    counter -= dotseen
    while len(cidrange) < 32:
        cidrange += '0'
    
    fcidrange = f'{int(cidrange[0:8], 2)}.{int(cidrange[8:16], 2)}.{int(cidrange[16:24], 2)}.{int(cidrange[24:32],2)}/{counter}'
    if not final:
        file1.write(f'{fcidrange}\n')
    else:
        file1.write(f'{fcidrange}')

    
    
                    
count = int(input(''))
for i in range(0, count):
    solve(i == count-1)    
    
file1.close()
