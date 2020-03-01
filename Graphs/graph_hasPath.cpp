#include<iostream>
using namespace std;
void hasPath(int **edges,int n,int sv,int en,bool *visited){
  visited[sv]=true;
  if(edges[sv][en]==1){
    cout << "true";
    exit(0);
  }
  for(int i=0;i<n;i++){
    if(sv==i){
      continue;
    }
    else if(edges[sv][i]==1){
      if(visited[i]){
        continue;
      }
      hasPath(edges,n,i,en,visited);
  }
}
 cout << "false";
  return;
}
int main()
{
  int n;
  int e;
  cin >> n >> e;
  int sv;
  int en;
  cin >> sv >> en;
  int** edges = new int*[n]; // Dynamically created two array
  for(int i = 0; i < n; i++)
  {
    edges[i] = new int[n];
    for(int j=0;j<n;j++)
    {
      edges[i][j]=0;
    }
  }
  for(int i=0;i<e;i++)
  {
    int f,s;
    cin >> f >> s;
    edges[f][s]=1;
    edges[s][f]=1;
  }
  bool *visited = new bool[n];
  for(int i=0;i<n;i++)
  {
    visited[i] = false;
  }
  hasPath(edges,n,sv,en,visited);
delete []visited;
  for(int i=0;i<n;i++){
    delete []edges[i];
  }
  delete []edges;
}
/*
5 8
0 1
0 4
1 2
2 0
2 4
3 0
3 2
4 3
4 1
*/
