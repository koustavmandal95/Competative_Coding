#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<int> v{10,20,30,40,50};
    cout <<"Vector contains :";
    for(unsigned int i =0;i< v.size();i++){
      cout << " " << v[i];
    }
    cout << "\n";
    vector<int>::iterator low1,low2;
    low1 = lower_bound(v.begin(),v.end(),35);
    low2 = lower_bound(v.begin(),v.end(),11);
    cout << *low1 << endl;
    cout << *low2 << endl;
    cout <<"\n the lower bound for element 35 "<< (low1 - v.begin()) << endl;
    cout <<"\n the lower bound for element 7 "<< (low2 - v.begin()) << endl;


}
