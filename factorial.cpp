#include<bits/stdc++.h>
using namespace std;
int fact(int N){
  if(N == 1){
    return 1;
  }
   int smallans = N*fact(N-1);
   return smallans;
}
int main(){
  int N;
  cin >> N;
  int ans = fact(N);
  cout << ans;
  return 0;
}
