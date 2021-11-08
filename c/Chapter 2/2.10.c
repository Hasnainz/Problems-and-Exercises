#include <stdio.h>

char lower(char c){
  return ((c >= 65) && (c <= 90)) ? c + 32 : c;
}
int main(){
  char meow[] = "The Cat Goes Meow MEONJFAOIHAIPHFOI 847u9374u29jihjfa98fy-23;f.,s";
  int a = 0;
  while(meow[a] != '\0'){
    printf("%c", lower(meow[a++]));
  }
  printf("\n");
  return 0;
}


