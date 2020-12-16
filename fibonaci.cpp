#include<bits/stdc++.h>
using namespace std;
int fibo(int N)
{
  if(N <= 0){
    return 0;
  }
  if(N ==1 || N ==2){
    return 1;
  }
  int ans = fibo(N-1)+fibo(N-2);
  return ans;
}
int main()
{
      int N;
      cin >> N;
      int ans = fibo(N);
      cout << ans << "\n";
}
