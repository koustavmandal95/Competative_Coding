#include<iostream>
using namespace std;
#define MAX 50000
class Euler
{
 int last_range;
 int arr[MAX];
public:
  Euler(int r=0):last_range(r)
  {

  }
  void set_arr()
  {
    for(int i=0;i<last_range;i++)
    {
      arr[i]=0;
    }
  }
  void process()
  {
    int i=1;
    int ans =0;
    while(i !=last_range)
    {
        ans = sum_all(arr,i);
        if( ans == i)
        {

            cout << " The number is :" << i << "\n";
        }
        i++;
    }
  }
int sum_all(int arr[], int i)
  {
    int sum =0;
    int rem = 0;
     while(i>0)
     {
         rem = i%10;
         //cout << find_factorial(arr,rem) << " "<<" The sum is " <<  sum <<"\n";
         sum = sum+ find_factorial(arr,rem);
         i = i/10;
     }

 return sum;
  }
  int find_factorial(int arr[],int N)
  {
      if(N ==1 || N==0)
      {
          return 1;
      }
      if(arr[N]!=0) // memorisation
      {
          return arr[N];
      }
     int fact =  N*find_factorial(arr,N-1);
     arr[N]=fact;
     return fact ;
  }
};
int main()
{
  Euler c1(50000);
  c1.set_arr();
  c1.process();
  return 0;

}
