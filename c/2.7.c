#include <stdio.h>

unsigned int invert(unsigned int x, int p, int n);

void showbits(unsigned int x){
  int i = 0;
  for(int i = (sizeof(int) * 8) - 1; i >= 0; i--){
    putchar(x & (1u << i) ? '1' : '0');
  }
  printf("\n"); 

}

int main(){
  unsigned int a = setbits(0b10110101, 6, 4, 0b1010);
  showbits(a);
  return 0;
}

unsigned int invert(unsigned int x, int p, int n){
  return 0;
}
