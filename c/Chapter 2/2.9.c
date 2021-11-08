#include <stdio.h>

int bitcount(unsigned x){
  unsigned int c;
  for(c = 0; x; ++c){
    x &= x - 1;
  }
  return c;
}
void showbits(unsigned int x){
  int i = 0;
  for(int i = (sizeof(int) * 8) - 1; i >= 0; i--){
    putchar(x & (1u << i) ? '1' : '0');
  }
  printf("\n"); 

}

int main(){
  printf("%d\n", bitcount(0b111000111000111111111111000));
  return 0;
}


