#include<iostream>
using namespace std;
class base{
  int i;
public:
  void set_i(int num)
  {
    i= num;
  }
  int get_i()
  {
    return i;
  }
};
class derived: public base{
  int j;
    void set_j(int num){ j = num;}
    int get_j(){return j;}
};
int main()
{
  base *bp;
  derived d;
  bp = &d; // base pointer points to derived object
  bp->set_i(10);
  cout << bp->get_i() << " ";
  return 0;
}
