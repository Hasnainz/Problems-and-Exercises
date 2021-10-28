#include <stdio.h>

int main()
{
    float fahr, celsius;
    float lower, upper, step;

    lower = 0.0;
    upper = 300.0;
    step = 4;

    celsius = lower;
    printf("celcius\tfahr\n");
    while (celsius <= upper) {
        fahr = 9.0/5.0*celsius+32.0;
        printf("%3.0f\t%6.1f\n", celsius, fahr);
        celsius += step;
    }
}