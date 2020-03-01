#include<bits/stdc++.h>
using namespace std;
int main()
{
  int N;
  cout << "Enter the number of rows : ";
  cin >> N;
  int arr[N];
  int store[N];
  for(int i=0;i<N;i++)
  {
    arr[i]=0;
    store[i]=0;
  }
  arr[0] = 1;
  for(int i=0;i<N;i++)
  {
    for(int j=1;j<i;j++)
    {
      store[j-1]=arr[j-1];
      store[j] = arr[j];
    }
    arr[i]=1;
    for(int k=0;k<N;k++)
    {
      cout << arr[k] << " " ;
    }
    cout << "\n";
  }

}
