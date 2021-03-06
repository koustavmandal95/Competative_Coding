#include<iostream>
using namespace std;
#include<unordered_map>
#include<vector>
bool hasPath_DFS(unordered_map<int,vector<int>*>&adjacencyList,int v1,int v2,unordered_map<int,bool>&visited){
  vector<int>*adjacencyVertices = adjacencyList[v1];
  for(int i=0;i<adjacentVertices->size();i++){
    if(adjacentVertices->at(i) == v2){
      return true;
    }
  }
  visited[v1] = true;
  for(int i=0;i<adjacentverticess->size();i++){
    if(visited.count(adjacentVertices->at(i))==0){
      bool ans = hasPath_DFS(adjacencyList,adjacentVertices->at(i),v2,visited);
      if(ans){
        return ans;
      }
    }
  }
  return false;
}
int main()
{
  int n,e;
  cin >> n >> e;
  unordered_map<int,vector<int>*>adjacencyList;
  for(int i=0;i<n;i++){
    vector<int>*v = new vector<int>;
    adjacencyList[i] = v;
  }
  int count =1;
  while(count <= e){
    int source,dest;
    cin >> source >> dest;
    adjacencyList[source]->push_back(dest);
    adjacencyList[dest]->push_back(source);
    count++;
  }
  int v1, v2;
  cin >> v1 >> v2;
  if(hasPath_DFS(adjacencyList,v1,v2)){
    cout << "true" << endl;
  }
  else{
    cout << "false" << endl;
  }
  return 0;
}
