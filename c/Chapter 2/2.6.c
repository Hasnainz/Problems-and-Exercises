#include <stdio.h>

unsigned setbits(unsigned int x,int p,int n,unsigned int y);

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

unsigned setbits(unsigned int x, int p, int n, unsigned int y){
  showbits(x);
  x |=  ~(~(0 << 1) << n) << (p-n+1);
  showbits(x);
  showbits(y);
  y = ~((~y & (~(~(0 << 1) << n))) << (p-n+1));
  showbits(y);
  return x & y;
}






