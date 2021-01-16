#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main(){
    vector<string> v;
    v.push_back("abc");
    v.push_back("hello");
    for(int i=0; i<v.size();i++){
      cout << v[i] << endl;
      sort(v[i].begin(),v[i].end());
      cout << v[i] << endl;
    }
    string s3;
    getline(cin,s3);
    cout << s3 << endl;
     cout << s3.length() << endl;
     string s4;
     s4="MERN";
     s4[0]='P';
     cout << s4 << endl;

     cout << s3+s4 << endl;

     string s5 ="abcabc";
     cout << s5.substr(0,3) << endl;

     cout << s5.find("cab") << endl;

     int a = 123;
     string s6 = to_string(a);
     s6[0] = '3';
     s6.push_back('8');
     cout << s6 << endl;

     a=atoi(s6.c_str()); // to integer
     cout << a << endl;

    return 0;
}
