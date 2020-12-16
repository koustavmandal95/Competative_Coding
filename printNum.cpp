#include<bits/stdc++.h>
using namespace std;
void printnum(int N,int count)
{
      if(N<count)
      {
        return;
      }
      cout << count << " ";
      printnum(N,count+1);
}
int main()
{
  int N ;
  cin >> N;
  int count=1;
  printnum(N,count);
}
