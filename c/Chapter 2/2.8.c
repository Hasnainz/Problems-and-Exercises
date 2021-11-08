#include <stdio.h>

#define INT_SIZE sizeof(int)
#define INTBITS INT_SIZE * 8 - 1

unsigned int rightrot(unsigned int x, int n);

void showbits(unsigned int x){
  int i = 0;
  for(int i = (sizeof(int) * 8) - 1; i >= 0; i--){
    putchar(x & (1u << i) ? '1' : '0');
  }
  printf("\n"); 

}

int main(){
  unsigned int a = rightrot(0b101101101, 2);
  showbits(a);
  return 0;
}

unsigned int rightrot(unsigned int x, int n){
  int dropped_bit;
  n %= sizeof(int) * 8 - 1;
  while(n--){
    dropped_bit = x & 1;
    x = (x >> 1) & (~(1 << INTBITS));
    x = x | (dropped_bit << INTBITS);
  }
  return x;
}
