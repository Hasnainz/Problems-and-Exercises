#include <stdio.h>

#define TRUE 1

int main(){
   int c, i;
   int w = 0;
   while ((c = getchar()) != '\n'){
        if(c != ' '){
           while(TRUE){
              ++w;
              c = getchar();
              if (c == ' ' || c == '\n') break;
           }
           for(i = 0; i < w; ++i){
              printf("=");
           }
           printf("\n");
           w = 0;
        }
   } 
}
    
