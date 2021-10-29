#include <stdio.h>

double celsiusToFahr(double c);


int main(){

   float fahr, celsius;
   float lower, upper, step;

   lower = 0.0;
   upper = 300.0;
   step = 50;

   celsius = lower;
   printf("celsius\tfahr\n");
   while (celsius <= upper) {
      printf("%3.0f\t%6.1f\n", celsius, celsiusToFahr(celsius));
      celsius += step;
   }

   return 0;
}

double celsiusToFahr(double celsius){
   return 9.0/5.0*celsius+32.0;
}
    
