#include <stdio.h>

#define MAX 50

int getLine(char s[], int lim);
void decomment(char line[]);

int main() {
    int c;
    char line[MAX];

    while((c = getLine(line, MAX)) > 0){
        decomment(line);
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

void decomment(char line[]){
    int ch = 1;
    int pch = 0;
    int i = 0;
    
    while(1){
        ch = line[i++];
        if(ch == '/' && pch == '/'){ //Check if there are two // next to each other
            line[i-2] = '\n'; //Add a newline to the first /
            line[i-1] = '\0'; //Add a null to the second
        }
        pch = ch;
        if(ch == '\0') break; //If we reach the end of the line, break
    }
}