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
  store[0] =1;
  arr[0]=1;
  for(int i=0;i<N;i++)
  {
    for(int j=1;j<i;j++)
    {
      arr[j] = store[j-1]+store[j];
    }
    arr[i]=1;
    for(int k=0;k<N;k++)
    {
      store[k]=arr[k];
      cout << arr[k] << " " ;
    }
    cout << "\n";
  }

}
