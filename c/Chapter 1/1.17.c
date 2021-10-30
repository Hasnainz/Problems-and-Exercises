#include <stdio.h>
#define MAXLINE 100 // The max is n-1 chars because the last char will be the terminator \0

int getLine(char line[], int maxline);
void copy(char to[], char from[]);

int main() {
    int len, i;

    char line[MAXLINE];
    while ((len = getLine(line, MAXLINE)) > 0){
        if (len > 80) {
            printf("%s has %d characters which is more than 80\n", line, len);
        }
    }

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

    //If there are still characters to be read, increase len
    while( (c = getchar()) != '\n' && c != EOF) ++i;

    return i;
}
