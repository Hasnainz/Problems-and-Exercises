#include <stdio.h>
/*Steps

    Step 1 − Divide the decimal number to be converted by the value of the new base.

    Step 2 − Get the remainder from Step 1 as the rightmost digit (least significant digit) of new base number.

    Step 3 − Divide the quotient of the previous divide by the new base.

    Step 4 − Record the remainder from Step 3 as the next digit (to the left) of the new base number.

Repeat Steps 3 and 4, getting remainders from right to left, until the quotient becomes zero in Step 3.*/
void reverse(char s[]){
  int e = 0;
  while(s[e++] != '\0');
  e -= 2;
  int i = 0;
  for(;i < e;i++, e--){
    char temp = s[i];
    s[i] = s[e];
    s[e] = temp;
  }
 
}

void itob(int n, char s[], int b){
  int i = 0;
  int sign = n;
  do{
    int d = n % b;
    if(d <= 9) s[i++] = d + '0'; 
    else s[i++] = d + 'a' - 10;
  }while((n /= b) > 0);
  
  if(sign < 0) s[i++] = '-';
  s[i] = '\0';
  reverse(s);
}

int main(){
  int n = 96907;
  char s[100];
  int b = 16;
  itob(n, s, b);
  printf("%s\n", s);
  b = 2;
  itob(n, s, b);
  printf("%s\n", s);

  
  return 0;
}


