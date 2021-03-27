file1 = open("out.txt","w") 


def solve(final):
    key_count = int(input(''))
    cipher_text = input('')
    keys = []
    for i in range(0, key_count):
        keys.append(input(''))
    counter = 0
    for key in keys:
        counter += 1
        result = ""
        for i in range(0, 128, 2):
            a = (int(cipher_text[i:i+2], 16))
            b = (int(key[i:i+2], 16))
            #print(f'a:{a}, b:{b}')
            result += chr(a^b)
        if counter == key_count and final:
            file1.write(f'[{result}]')
        else:
            file1.write(f'[{result}]\n')

count = int(input(''))
for i in range(0, count):
    solve(i == count-1)    
    

file1.close()
