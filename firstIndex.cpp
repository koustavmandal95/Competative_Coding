#include<bits/stdc++.h>
using namespace std;
int firstPosition(int arr[] , int N , int element,int i){
  if(i==N){
    return -1;
  }
  if(arr[i] == element ){
      return i;
  }
  return firstPosition(arr,N,element,i+1);
}
using namespace std;
int main(){
  int N,element;
  cin >> N >> element;
  int *arr = new int[N];
  for(int i=0; i<N;i++){
    cin >> arr[i];
  }
  int ans = firstPosition(arr,N,element,0);
  cout << " The first index is " << ans << "\n";
  delete[] arr;
  return 0;
}
/*
>o/p
7 ==>N
6 ==> element
23
43
6
32
6
89
456
 The first index is 2

>o/p
4 => N
5 => element
12
34
55
89
 The first index is -1
 */
