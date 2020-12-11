#include<bits/stdc++.h>
using namespace std;
int countDigits(int N)
{
    if(N%10 == 0)
    {
      return ;
    }
    count++;
    int ans = countDigits(N%10,count);
    return ans;
}
int main()
{
  int N ;
  cin >> N;
  int count = 0;
  int ans = countDigits(N,count);
  cout << ans << "\n";
}
