#include <stdio.h>

int main()
{
    int c;
    while ((c = getchar()) != '\n'){
        if(c == '\t') printf("\\t");
        else if (c == '\b') printf("\\b");
        else if (c == '\\') printf("\\\\");
        else putchar(c);
    }
    printf("\n");
}