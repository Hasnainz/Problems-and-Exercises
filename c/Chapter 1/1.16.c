#include <stdio.h>
#define MAXLINE 10 // The max is n-1 chars because the last char will be the terminator \0

int getLine(char line[], int maxline);
void copy(char to[], char from[]);

int main() {
    int len;
    int max;
    int i;
    char line[MAXLINE];
    char longest[MAXLINE];
    max = 0;
    while ((len = getLine(line, MAXLINE)) > 0)
    if (len > max) {
        max = len;
        copy(longest, line);
    }
    //Replace the newline character with a 
    for (i = 0; i < MAXLINE; ++i){
        if(longest[i] == '\n'){
            longest[i] = '\\';
        }
    }

    if (max > 0)
        printf("%s with %d characters\n", longest, max);
    return 0;
}

int getLine(char s[], int lim){
    int c, i;

    for (i = 0; i < lim-1 && (c = getchar()) != EOF && c != '\n'; ++i)
        s[i] = c;

    if (c == '\n') {
        s[i] = '\\';
        ++i;
    }

    s[i] = '\0'; //End of line

    //If there are still characters to be read, increase the size
    while( (c = getchar()) != '\n' && c != EOF) ++i;

    return i;
}
void copy(char to[], char from[])
{
    int i;
    i = 0;
    while ((to[i] = from[i]) != '\0')
        ++i;
}