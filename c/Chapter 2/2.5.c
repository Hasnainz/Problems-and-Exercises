#include <stdio.h>
#include <ctype.h>

int any(char s1[], char s2[]);
int in(char c, char b[]);

int main(){
    printf("%d\n", any("The cat goes meow", "m"));
}

int in(char c, char b[]){
    int a = 0;
    while(b[a] != '\0'){
        if (b[a++] == c)
            return 1;
    }
    return 0;
}

int any(char a[], char b[]){
    int i = 0;
    while(a[i] != '\0')
        if(in(a[i++], b))
            return i-1;
    return -1;
}

