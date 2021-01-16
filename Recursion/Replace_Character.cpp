#include<bits/stdc++.h>
using namespace std;
void ReplaceCharacter(string s ,string str , char replacer, char replace){
    if(str.length() == 0){
      cout <<s << "\n";
      return;
    }
    if(str[0] == replace){
      str[0] = replacer;
        s=s+str[0];
    }
    else{
      s=s+str[0];
    }
    ReplaceCharacter(s,str.substr(1),replacer,replace);

}
int main(){
  char replacer,replace;
  string str;
  replace = 'b';
  replacer='y';
  getline(cin,str);
  string s="";
  ReplaceCharacter(s,str,replacer,replace);
  return 0;
}
