#include <stdio.h>

void escape(char s[], char t[]){

  int i;
  int j = 0;

  for(i = 0; t[i] != '\0'; ++i){
    switch(t[i]){
      case '\n':
        s[j++] = '\\';
        s[j++] = 'n';
        break;
      case '\t':
        s[j++] = '\\';
        s[j++] = 't';
        break;
      default:
        s[j++] = t[i];
        break;
    }
  }
}

int main(){
  char t[] = "\tMeow\nGoes\tthe\nCat";
  char s[100];
  escape(s, t);
  printf("%s\n", s);
  return 0;
}


