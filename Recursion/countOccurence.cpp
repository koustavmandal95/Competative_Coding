#include<bits/stdc++.h>
using namespace std;
int countOccurence(int arr[],int N,int element,int count){
  if(N==0){
    return count;
  }
  if(arr[N-1] == element){
    count++;
  }
  countOccurence(arr,N-1,element,count);
}
int main(){
  int N , element;
  cin >> N >> element;
  int *arr = new int[5];
  for(int i=0;i<N;i++){
    cin>>arr[i];
  }
  cout << countOccurence(arr,N,element,0);
  delete[] arr;
  return 0;
}
/*
5 5  size , element search
5 5 5 5 6
4  => 5 times 5
*/
