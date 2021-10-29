#include <stdio.h>

int main()
{
    int c;
    while ((c = getchar()) != EOF) { 
        if( c != '\n' && c != ' ' && c != '\t'){
           while(c != '\n' && c != ' ' && c != '\t'){
               putchar(c);
               c = getchar();
           }
           putchar('\n');
        }
    } 
}
