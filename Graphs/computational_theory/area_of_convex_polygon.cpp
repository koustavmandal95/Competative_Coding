#include<bits/stdc++.h>
using namespace std;
double PolygonArea(double X[],double Y[],int n){
  int j = n-1;
  int farea =0;
  double cross_prod=0;
  for(int i=0;i<n;i++){
    cross_prod=X[j]*Y[i]-Y[j]*X[i];
    j=i;
    farea= farea+cross_prod;
  }
    return abs(farea/2);
}
int main(){
  int n;
  cin >> n;
  double X[n];
  double Y[n];
  for(int i=0; i<n;i++){
    cin >> X[i];
  }
  for(int i=0; i<n;i++){
    cin >> Y[i];
  }
  cout << PolygonArea(X,Y,n);
}
