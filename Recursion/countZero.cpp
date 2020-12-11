#include<bits/stdc++.h>
using namespace std;
int countZero(int number,int ans){
  if(number/10 == 0){
    return ans;
  }
  if(number%10 == 0){
    ans=ans+1;
  }
  countZero(number/10,ans);
}
int main(){
  int number ;
  cin >> number;
  cout << countZero(number,0);
}
