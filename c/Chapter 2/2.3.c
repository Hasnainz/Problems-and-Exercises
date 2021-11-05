#include <stdio.h>
#include <ctype.h>

int htoi(char hex[]);

int main(){
    char a[] = "0x7F"; 
    printf("%d\n", htoi(a));
    return 0;
}


int htoi(char hex[]) {
    int val = 0;
    int i = 0;
    while (hex[i] != '\0') {
        // get current character then increment
        int byte = hex[i++];
        // transform hex character to the decimal
        //We only want to perform the bitwise operation on valid chars
        if (byte >= '0' && byte <= '9'){
            byte = byte - '0';
            val = (val << 4) | byte;
        } 
        else if (byte >= 'a' && byte <='f'){
            byte = byte - 'a' + 10;
            val = (val << 4) | byte;
        }
        else if (byte >= 'A' && byte <='F'){
             byte = byte - 'A' + 10;
             val = (val << 4) | byte;
        }
    }
    return val;
}

