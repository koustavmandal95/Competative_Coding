#include<bits/stdc++.h>
using namespace std;
int pow(int N,int base)
{
      if(base == 0)
      {
        return 1;
      }
      int ans = N*pow(N,base-1);
      return ans;
}
int main(){
  int N;
  int base;
  cin >> N >> base;
  int ans = pow(N,base);
  cout << ans << "\n";
}
