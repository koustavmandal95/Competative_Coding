#include<bits/stdc++.h>
using namespace std;
int lastIndex(int arr[],int N,int element){
  if(N == 0){
    return -1;
  }
  if(arr[N-1] == element){
    return N-1;
  }
  return lastIndex(arr,N-1,element);
}
int main(){
  int N,element;
  cin >> N >> element;
  int *arr = new int[N];
  for (size_t i = 0; i < N; i++) {
      cin >> arr[i];
  }
  int ans = lastIndex(arr,N,element);
  cout << " The last Index " << ans << "\n";
  delete[] arr;
}
