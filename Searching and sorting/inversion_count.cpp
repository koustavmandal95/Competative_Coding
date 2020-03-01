#include<bits/stdc++.h>
using namespace std;
long long merge(int A[],int left, int mid,int right){
  int i = left, j=mid,k=0;
  int temp[right-left+1];
  while(i<mid && j<=right){
    if(A[i] <= A[j]){
      temp[k++] = A[i++];
    }else{
      temp[k++] = A[j++];
    }
  }
}
long long merge_sort(int A[],int left, int right){
  long long count =0;
  if(right > left){
    int mid = (left+right)/2;

    long long countLeft = merge_sort(A,left,mid);
    long long countRight = merge_sort(A,mid+1,right);
    long long mycount = merge(A,left,mid+1,right);
  }
}
long long solve(int A[],int n){
  long long ans = merge_sort(A,0,n-1);
  return ans;
}
int main()
{
  return 0;
}
