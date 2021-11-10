#include <stdio.h>

void expand(char s1[], char s2[]){
  int i, j, k;
  i = 0;
  j = 0;

  int len = 0;
  while(s1[len++] != '\0');
  len--;

  while(s1[i] == '-'){
    s2[j] = '-';
    ++i;
    ++j;
  }  
  while(s1[i] != '\0' && s1[i] != '-'){
    for(k = s1[i];k <= s1[i+2];j++, k++){
      s2[j] = k;
    }
    i += 2;
    if(i >= len) break;
  }
  i--;
  if(s1[i] == '\0') return;
  while(s1[i] == '-'){
    s2[j] = '-';
    i++;
    j++;
  }
  s2[j] = '\0';

}

int main(){
  char s[] = "-----------a-b-k-j-z-0-9----";
  char t[1000];
  expand(s, t);
  printf("%s\n", t);
  return 0;
}


