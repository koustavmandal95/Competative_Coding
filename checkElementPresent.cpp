#include<bits/stdc++.h>
using namespace std;
bool isPresent(int arr[],int N,int element){
    if(N == 0){
      return false;
    }
    if(arr[N-1] == element){
      return true;
    }
    bool ans = isPresent(arr,N-1,element);
    return ans;
}
int main(){
  int N;
  int element;
  cin >> N >> element;
  int *arr = new int[N];
  for(int i=0; i<N;i++){
    cin >> arr[i];
  }
  int ans = isPresent(arr,N,element);
  if(ans){
    cout << " Is Present ";
  }else{
    cout << " Not present ";
  }
  delete[] arr;
  return 0;
}
