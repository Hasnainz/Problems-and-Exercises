read = open('in.txt', 'r', encoding="utf8")
write = open('out.txt', 'w')



# def solve(index, final):
#     a,b = read.readline.strip().split(' ')
#     write.write(f'{a + b}')



# count = int(read.readline().strip())
# for i in range(0, count):
#     solve(i+1, i == count-1)

a = read.readlines()
for line in a:
    b, c = [int(x) for x in line.strip().split(' ')]
    write.write(f'{b + c}\n')