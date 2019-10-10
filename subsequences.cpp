#include<bits/stdc++.h>
using namespace std;
int subs(string input, string output[])
{
    if(input.empty())
    {
        output[0]="%";
        return 1;
    }
    string smallString=input.substr(1);
    cout << "before completing all recursion---" << smallString << endl;
    int smallOutputSize=subs(smallString,output);
    cout << "-------after recursion-----"<< smallString << endl;
    cout << "the smallStringsize--" << smallOutputSize << endl;   
    for(int i=0; i < smallOutputSize;i++)
    {   cout << i<< "--" << output[i] << "   The value of input[%d] is  "<< input[0] << endl;
        output[i+smallOutputSize]=input[0]+output[i];
        cout << i<< "--" << output[i+smallOutputSize] << "   The value of input[%d] is  "<< input[0] << endl;
    }
    return 2*smallOutputSize;
}
int main()
{
    string input;
    cin >> input;
    string* output = new string[1000];
    int count = subs(input,output);
    cout << "-----------------------------------"<< endl;
    cout << count << endl;
    for(int i=0;i<count;i++)
    {
        cout << output[i] << endl;
    }
}