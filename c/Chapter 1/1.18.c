#include <stdio.h>
#define MAXLINE 100 // The max is n-1 chars because the last char will be the terminator \0

int getLine(char line[], int maxline);
void trim(char line[]);

int main() {
    int len, i;

    char line[MAXLINE];
    while((len = getLine(line, MAXLINE)) > 0){
        trim(line);
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
void trim(char a[]){
    int i;
    for(i = MAXLINE; i >= 0 && (i == ' ' || i == '\n' || i == '\n'); --i){
        a[i] = '\0';
    }
}