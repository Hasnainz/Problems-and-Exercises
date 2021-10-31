#include <stdio.h>

int main() {
    int c;
    int s = 0;
    //Not very intelligent line wrapping
    while((c = getchar()) != EOF){
        putchar(c);
        
        if(c != '\n') ++s;
        else if(c == '\t') s += 4;
        else s = 0;
        
        if(s > 10){
            putchar('\n');
            s = 0;
        } 
    }
    return 0;
}
