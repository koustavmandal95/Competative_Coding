#include<bits/stdc++.h>
using namespace std;
int power(int base,int p){
  if(p ==0){
    return 1;
  }
  return base*power(base,p-1);
}
float gsum(int k){
  if(k ==0){
    return 1.0;
  }
  float smallans = 1.0/(power(2,k))+gsum(k-1);
  return smallans;
}
int main(){
  int k;
  cin >> k;
  cout << gsum(k);
}
