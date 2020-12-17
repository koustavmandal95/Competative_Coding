#include<bits/stdc++.h>
using namespace std;
bool palindrome(int arr[],int start,int end){
  if(start >= end){
    return true;
  }
  if(arr[start] != arr[end-1]){
    return false;
  }
  palindrome(arr,start+1,end-1);
}
int main(){
  int N ;
  cin >> N;
  int *arr = new int[N];
  for(int i=0; i<N;i++){
    cin >> arr[i];
  }
  palindrome(arr,0,N) == 1 ? cout << "palindrome": cout << "Not palindrome";
  delete[] arr;
  return 0;
}
/*
4
1 0 0 1
palindrome
*/
