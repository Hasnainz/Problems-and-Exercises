#include <stdio.h>
#include <limits.h>
#include <float.h>

// #define VTAB '\013'
// #define BELL '\007'
// #define VTAB '\xb'
// #define BELL '\x7'

enum boolean { NO, YES };
enum months { JAN = 1, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC };

int main(){
    int isThisHex = 0xF;
    printf("Hex F in decimal : %d\n", isThisHex);
    isThisHex = 017;
    printf("Oct 17 in decimal : %d\n", isThisHex);
    unsigned long ulong = 1000ul;

    printf("Does this " "concatenate?\n"); // IT DOES!
    printf("%d\n", MAY);
    return 0;
}