#include <stdio.h>
#include <math.h>

int isSpace(int a){
  return (a == ' ' || a == '\t');
}
int isDigit(int a){
  return (a >= '0' && a <= '9');
}

double atof(char s[]){
  double val, power;
  int i, sign;

  for(i = 0; isSpace(s[i]); i++);
  sign = (s[i] == '-') ? -1 : 1;
  if(s[i] == '-' || s[i] == '+') 
    i++;
  for(val = 0.0; isDigit(s[i]); i++)
    val = 10.0 * val + (s[i] - '0');
  if(s[i] == '.')
    i++;
  for(power = 1.0; isDigit(s[i]); i++){
    val = 10.0 * val + (s[i] - '0');
    power *= 10;
  }

  if(s[i] == 'e'|| s[i] == 'E')
    i++;
  int esign = (s[i] == '-') ? -1 : 1;
  if(s[i] == '-' || s[i] == '+')
    i++;
  double exponent;
  for(exponent = 0.0; isDigit(s[i]); i++)
    exponent = 10 * exponent + (s[i] - '0');
  
  return sign * val / power * pow(10, esign * exponent);
 
}

int main(){
  printf("%f\n", atof("      123.2537843e-2"));
  return 0;

}


