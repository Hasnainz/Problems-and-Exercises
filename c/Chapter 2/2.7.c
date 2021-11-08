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
  unsigned int a = invert(0b10110101, 4, 3);
  showbits(a);
  return 0;
}

unsigned int invert(unsigned int x, int p, int n){
  return x ^ ~(~(0 << 1)<<n)<<p-n+1;  
}
