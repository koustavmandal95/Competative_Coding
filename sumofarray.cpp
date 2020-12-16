#include<bits/stdc++.h>
using namespace std;
int sumArray(int arr[], int N){
  if(N == 0){
    return 0 ;
  }
  int smallans = arr[N-1]+sumArray(arr,N-1);
  return smallans;
}
int main(){
  int N;
  cin >> N;
  int *arr = new int[N];
  for(int i =0; i<N;i++){
    cin >> arr[i];
  }
  int ans = sumArray(arr,N);
  cout << ans ;
  delete[] arr;
  return 0;
}
