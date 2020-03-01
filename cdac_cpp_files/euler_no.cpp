#include<iostream> //Koustav Mandal  "ALL codes are garbage"
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
int sum_all(int arr[],int i)
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
int main()
{
    cout << " Enter the ending range : " ;
    int N;
    cin >> N;
    int arr[N+1];
    for(int i =0 ; i<N+1;i++)
    {
        arr[i]=0;
    }
    int i=1;
    int ans =0;
    while(i !=(N+1))
    {
        ans = sum_all(arr,i);
        if( ans == i)
        {

            cout << " The number is :" << i << "\n";
        }
        i++;
    }
    return 0;

}
