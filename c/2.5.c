#include <stdio.h>
#include <ctype.h>

int any(s1[], s2[]);
int in(char c, char b[]);

int main(){

}

int in(char c, char b[]){
    int a = 0;
    while(b[a] != '\0'){
        if (b[a++] == c)
            return 1;
    }
    return 0;
}

void any(char a[], char b[]){

}

