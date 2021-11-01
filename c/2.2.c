#include <stdio.h>
#include <limits.h>
#include <float.h>

int main(){
    int isThisHex = 0xF;
    printf("Hex F in decimal : %d\n", isThisHex);
    isThisHex = 017;
    printf("Oct 17 in decimal : %d\n", isThisHex);
    unsigned long ulong = 1000ul;
    return 0;
}