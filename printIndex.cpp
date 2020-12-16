#include<bits/stdc++.h>
using namespace std;
void printIndex(int arr[],int N,int element,int i){
  if(N==i){
    return;
  }
  if(arr[i] == element){
    cout << i << " ";
  }
  printIndex(arr,N,element,i+1);
}
int main(){
  int N,element;
  cin >> N >> element;
  int *arr = new int[N];
  for(size_t i =0;i<N;i++){
    cin >> arr[i];
  }
  printIndex(arr,N,element,0);
  delete[] arr;
}
/*
7 ===> N (size of array)
5 ==> element to find the index.
10
5
83
5
-5
5
5
1 3 5 6

*/
