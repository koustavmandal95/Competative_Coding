#include<bits/stdc++.h> // Koustav Mandal 
using namespace std;
float factorial(int n)
{
  if(n==0 || n==1)
  {
    return 1;
  }
  int fact = n*factorial(n-1);
  return fact;
}
float power(int base, int n){
  if(n==0)
  {
    return 1;
  }
  else
  {
    float partial = power(base,n/2);
    float result = partial*partial;
    if(n%2==1)
    {
      result = result*base;
      }
      return result;
  }
}
int main()
{
  float degree;
  cout << "Enter the the angle in degrees :" ;
  cin >> degree;
  float radian=degree*(3.14/180);
  float series[5];
  series[0] = radian;
  float ans=0;
  cout << "The radian is " << radian << "\n";
  for(int i=1;i<=5;i++)
  {
    float num_power = power(series[0]*1000,2*i+1) ;
    float dem_power = power(1000,2*i+1);
    float summa=(num_power/dem_power)/factorial(2*i+1);
    // cout << ((power(-1,i))*power(series[0],(2*i)+1))/factorial((2*i)+1) << "\n" ;
    series[i] = series[i-1]+((power(-1,i))*summa);
  }
  cout<<"Sine of an angle is : "<<series[5]<< endl;
  return 0;
}
