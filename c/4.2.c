#include <stdio.h>

int strindex(char s[], char t[]){
  int k;
  int i = 0;
  int j = 0;
  while(s[i++] != '\0');
  while(t[j++] != '\0');
  j -= 2;
  k = j;
  while(i > 0){
    if(s[i] == t[j]){
      while(k >= 0){
        if(s[--i] != t[--k]) break;
        if(k == 0) return i;
      }
      k = j;
    }
    --i;
  }
  return -1;
}

int main(){
  int a = strindex("Cat This is Cat a string where the goes Cat meow", "Cat");
  printf("%d\n", a);
  return 0;
}


