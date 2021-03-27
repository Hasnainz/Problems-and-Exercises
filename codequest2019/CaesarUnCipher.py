file1 = open("out.txt","w") 

def solve():
    shift = int(input(''))
    ciphertext = input('')

    while shift >= 26:
        shift -= 26
    
    result = ""
    for ch in ciphertext:
        if ord(ch) == 32:
            result += ' '
        else:
            newChar = ord(ch) - shift
            if newChar < 97:
                newChar += 26
            result += chr(newChar) 
    file1.write(f'{result}\n')

count = int(input(''))
for i in range(0, count):
    solve()
    

file1.close()
