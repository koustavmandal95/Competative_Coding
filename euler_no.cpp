#include<iostream>
using namespace std;
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
void sum_all(int arr[],int i)
{
       int check_value = i;
       int sum =0;
        while(i/10 != 0)
        {
            if ( sum == check_value )
            {
                cout << " The number is euler : " << check_value << "\n";
            }
            cout << find_factorial(arr,i%10) << " "<<" The sum is " <<  sum <<"\n";
            sum = sum+ find_factorial(arr,i%10);
            i = i/10;
        }

    return ;
}
int main()
{
    int N;
    cin >> N;
    int arr[N+1];
    for(int i =0 ; i<N+1;i++)
    {
        arr[i]=0;
    }
    int i=1;
    while(i !=N)
    {
        sum_all(arr,i);
        i++;
    }
    return 0;
    
}
