#include<bits/stdc++.h>
using namespace std;
bool isSortedAscending(int arr[],int N){
  if(N==0 || N ==1){
    return true;
  }
  if(arr[N-2] > arr[N-1]){
    return false;
  }
  bool ans = isSortedAscending(arr,N-1);
  return ans;
}
bool isSortedDescending(int arr[],int N){
    if(N == 0 || N == 1){
      return true;
    }
    if(arr[N-2] < arr[N-1]){
      return false;
    }
    bool ans = isSortedDescending(arr,N-1);
    return ans;
}
int main(){
  int i , N;
  cin >> N;
  int *arr = new int[N];
  for(i=0;i<N;i++){
    cin >> arr[i];
  }
  bool ans1 = isSortedAscending(arr,N);
  bool ans2 = isSortedDescending(arr,N);
  if(ans1 == 1 || ans2 == 1){
    if(ans2){
          cout << "Is Sorted descending.";
    }
    else{
      cout << "Is Sorted ascending.";
    }
  }
  else{
    cout << "Not Sorted";
  }
  delete []arr;
  return 0;
}
