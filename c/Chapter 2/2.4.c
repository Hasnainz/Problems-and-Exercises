#include <stdio.h>
#include <ctype.h>

void squeeze(char a[], char b[]);
int in(char c, char b[]);

int main(){
    char a[] = "the cat goes meow";
    char b[] = "the cat goes";
    squeeze(a, b);
    printf("%s\n", a);
    return 0;
}

int in(char c, char b[]){
    int a = 0;
    while(b[a] != '\0'){
        if (b[a++] == c)
            return 1;
    }
    return 0;
}
//deletes each char in a that matches any char in b
void squeeze(char a[], char b[]){
    int i, j;
    i = j = 0;
    while(a[i] != '\0'){
        //If the current char of a is not in b then write it into else skip
        if(!(in(a[i], b))) a[j++] = a[i++];
        else ++i;
    }
    a[j] = '\0';
}

