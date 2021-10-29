#include <stdio.h>

int main()
{
    int c;
    while ((c = getchar()) != '\n'){
        if(c == ' '){
            putchar(c);
            while(c == ' ') c = getchar();
            putchar(c);
        }
        else putchar(c);
    }
    printf("\n");
}