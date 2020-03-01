#include<bits/stdc++.h>
using namespace std;
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


