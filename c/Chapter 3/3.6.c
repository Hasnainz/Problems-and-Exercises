#include <stdio.h>
#include <limits.h>

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

void itoa(int n, char s[], int m){
  int i;
  long sign = (long)n;
  long o = sign;

  if ((sign) < 0) /* record sign */
  {
    o = -o; /* make n positive */
  }
  i = 0;
  do {  /* generate digits in reverse order */
    s[i++] = o % 10 + '0'; /* get next digit */
  } while ((o /= 10) > 0); /* delete it */

  if (sign < 0)
  s[i++] = '-';
  s[i] = '\0';
  reverse(s);
  while(i+1 <= m) s[i++] = ' ';
  s[i] = '\0';
}

int main(){
  int numberi = INT_MIN; 
  int a = -11294;
  char number[100];
  itoa(a, number, 14);
  printf("%scat\n", number);
  return 0;
}


