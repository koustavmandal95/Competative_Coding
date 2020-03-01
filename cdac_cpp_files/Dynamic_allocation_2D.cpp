#include<bits/stdc++.h>
using namespace std;
void print(int **matrix, int n)
{
    for(int i=0;i<n;i++)
    {
        for(int j=0; j<n;j++)
        {
            cout << matrix[i][j] << "  ";
        }
        cout << "\n" ;
    }
}
void fill_all(int **matrix, int n)
{
      int row = n;
      int col = n;
    for ( int i=1; i<=n; i++)
    {
      if (matrix[0][col/2+i] ==0)
      {
          matrix[0][col/2+i]=i;
      }
      else if(matrix[n-1+i][col/2+1+i]==0)
      {
         matrix[n-1][col/2+1] = i; 
      }
    }
    print(matrix,n);

}
void fill_all(int **matrix, int n)
{
        for(int i =0;i<n;i++){
        for(int j=0;j<n;j++)
        {
            cout << " " << matrix[i][j];
        }
        cout <<"\n";
    }

    return;
}
int main()
{
    int N;
    cin >> N;
    int **matrix = new int*[N];
    for(int i =0;i<N;i++){
        for(int j=0;j<N;j++)
        {
            matrix[i][j] = 0;
        }
    }
    fill_all(matrix,N);
      for(int i=0;i<N;i++){
    delete []matrix[i];
  }
  delete []matrix;
}


