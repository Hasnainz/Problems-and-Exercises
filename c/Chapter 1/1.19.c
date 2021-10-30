#include <stdio.h>
#define MAXLINE 100 // The max is n-1 chars because the last char will be the terminator \0

int getLine(char line[], int maxline);
void reverse(char line[]);

int main() {
    int len, i;

    char line[MAXLINE] = "Hello World";

    while((len = getLine(line, MAXLINE)) > 0){
        reverse(line);
        printf("%s", line);
    }

    return 0;
}

int getLine(char s[], int lim){
    int c, i;

    for (i = 0; i < lim-1 && (c = getchar()) != EOF && c != '\n'; ++i)
        s[i] = c;

    if (c == '\n') {
        s[i] = '\n';
        ++i;
    }

    s[i] = '\0'; //End of line

    return i;
}

void reverse(char line[]){
    //line ends in a \n char so if the first element is the end then return
    if(line[0] == '\n') return;

    //Count length of the string
    int l = 0;
    while(line[l] != '\n') ++l;
    
    //Make a new array of the same size and decrement l so we don't copy \n as the first character
    char temp[l--];
    //Copy the end of the original array into the first of the temp array, increment then repeat
    int i = 0;
    while(l >= 0){
        temp[i] = line[l];
        --l;
        ++i;
    }
    //Add a new line to the end since we don't want to flip it
    temp[i] = '\n';
    //Comy the temp array into the original
    l = 0;
    while(l <= i){
        line[l] = temp[l];
        ++l;
    }
}