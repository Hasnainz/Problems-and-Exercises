#include <stdio.h>

#define MAX 50

int getLine(char s[], int lim);
void detab(char line[]);

int main() {
    int c;
    char line[MAX];

    while((c = getLine(line, MAX)) > 0){
        detab(line);
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

void detab(char line[]){
    int max = MAX*4;
    //Make a new array where the size is assuming all the characters are tabs.
    char temp[max];
    int i = 0;
    int j = 0;
    //Go through the line and replace each tab with 4 spaces and everything else is the same.
    for(i = 0; i < MAX; ++i){
        if(line[i] == '\t'){
            int k = j + 4;
            for(;j < k; ++j){
                temp[j] = ' ';
            }
            temp[j] = line[++i];
        }
        else{
            temp[j] = line[i]; 
        }
        ++j;
    }

    //Place an ending on the array
    temp[j] = '\0';
    i = 0;
    //Copy as much of the temporary array into the line
    while(temp[i] != '\0' && i < MAX-2){
        line[i] = temp[i];
        ++i;
    }
    //Place an ending on the line
    line[i] = '\0'; 
}