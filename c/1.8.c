#include <stdio.h>

int main()
{
    int c, b, t, n;
    b = 0;
    t = 0;
    n = 0;
    while ((c = getchar()) != EOF){
        if (c == '\n')
            ++n;
        if (c == '\t')
            ++t;
        if (c == ' ')
            ++b;
    }
    printf("Blanks: %d Tabs: %d New Lines: %d\n", b, t, n);
}