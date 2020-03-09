#include<iostream>
#include<string.h>
using namespace std;
class stack_in
{
public:
	int top;
	int size;
	char arr[50];
	stack_in(int top, int size) :top(top),size(size)
	{

	}
	bool isfull()
	{
		if (top >= size)
		{
			return 1;
		}
		return 0;
	}
	void push(char val)
	{
		arr[++top] = val;
	}
	char pop()
	{
		return arr[top--];
	}
	void display()
	{
		for (int i = top; i >= 0; i--)
		{
			cout << arr[i] << "\n";
		}
	}
	friend void reverse(stack_in &S);
};
void reverse(stack_in &S)
{
	stack_in copy(S.top,S.size);
	for (int i =S.size; i>=0; i--)
	{
		//cout << S.pop();
		copy.arr[i] = S.pop();
	}
	for (int i=S.size;i>=0; i--)
	{
		cout << copy.pop();
	}
	cout << "\n";
	

}
int main()
{
	char s[50]="india is great";
	// great is india
	int len = strlen(s);
	stack_in stk(-1, len);
	for (int i = 0; i<=strlen(s); i++)
	{
		stk.push(s[i]);
	}
	stk.display();
	reverse(stk);
	return 0;
}
