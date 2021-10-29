#include <stdio.h>

int main(){
   int c, i, j;
   int cfreq[26];
   for(i = 0; i < 26; ++i) cfreq[i] = 0;

   while ((c = getchar()) != '\n'){
      if(c >= 65 && c <= 90){
         ++cfreq[c-65];
      }
      else if(c >= 97 && c <= 122){
         ++cfreq[c-97];
      }
   }
   
   for(i = 0; i < 26; ++i){
      printf("%c: ", i+65);
      for(j = 0; j < cfreq[i]; ++j){
         printf("*");
      }
      printf("\n");
   }

}
    
