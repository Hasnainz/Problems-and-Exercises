#include <stdio.h>

int binSearch1(int x, int v[], int n){
  int low, high, mid;

  low = 0;
  high = n - 1;

  while(low <= high){
    mid = (low + high)/2; 
    if (x < v[mid]) high = mid + 1;
    else if (x > v[mid]) low = mid + 1;
    else return mid;
  }
  return -1;
}

int binSearch2(int x, int v[], int n){
  int low, high, mid;
  low = 0;
  high = n-1;

  while(low < high){
    mid = (low + high)/2 + 1;
    if (x < v[mid]) high = mid - 1;
    else low = mid;
  }
  return x == v[low] ? low : -1;
}

int main(){
  int c[] = {1,2,3,4,5,6,7,8,9,10,11};
  printf("%d\n", binSearch2(5,c,11));
  return 0;
}


