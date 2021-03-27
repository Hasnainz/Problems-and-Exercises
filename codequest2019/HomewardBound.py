file1 = open("out.txt","w") 

def b_count(a, v):
    count = 0
    for b in a:
        for c in b:
            if v == c:
                count += 1
    return count

def find_index(a, v):
    for i in range(0, len(a)):
        for j in range(0, 2):
            if a[i][j] == v:
                return i

def solve():
    plane_rides = int(input(''))
    boarding_passes = []
    order = []
    for i in range(0, plane_rides):
        boarding_passes.append(input('').split(" "))
    for i in range(0, len(boarding_passes)):
        find = False
        for j in range(0, 2):
            #print(f'i:{i} j:{j}')
            a = b_count(boarding_passes, boarding_passes[i][j])
            #print(f'boarding_passes:{boarding_passes}')
            #print(f'boarding_passes[i][j]:{boarding_passes[i][j]}')
            #print(f'a:{a}')
            if a == 1 and j == 1:
                find = True
                nxt_idx = i
                while len(boarding_passes) > 0:
                    order.append(boarding_passes[nxt_idx][1])
                    nextCountry = boarding_passes[nxt_idx][0]
                    order.append(nextCountry)
                    del boarding_passes[nxt_idx]
                    nxt_idx = find_index(boarding_passes, nextCountry)
                    #print(f'next:index: {nxt_idx}')
                    
                break
        if find:
            break
    nodupes = list(dict.fromkeys(order))
    for item in nodupes:
        file1.write(f'{item}\n')




count = int(input(''))
for i in range(0, count):
    solve()    
    

file1.close()

