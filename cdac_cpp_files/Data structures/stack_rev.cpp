#include<iostream> // Don't drink and code!!
#include<string.h>
#include<ctype.h>
using namespace std;
class stack_in
{
public:
	int top;
	int size;
	char arr[50];
	stack_in(int top=-1, int size=-1) :top(top),size(size)
	{

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
	stack_in copy;
	for (int i=S.size;i>=0; i--)
	{

		//if(isblank(S.arr[i]))
		if(S.arr[i]=='-')
		{
			//cout << "The index i  " << i <<"\n";
			while(copy.top>=0)
			{
				cout << copy.pop();
			}
			cout<< S.pop();
			continue;
 		}
					//cout << "The index outside if  " << i <<"\n";
			copy.push(S.pop());
 	}
	while(copy.top>=0)
	{
		cout << copy.pop();
	}
}
int main()
{
	char s[50]="Money-is-motivation";
	cout << s<<"\n";
	cout << "---------------------\n";
	// great is india
	int len = strlen(s);
	stack_in stk(-1, len-1);
	for (int i = 0; i<strlen(s); i++)
	{
		stk.push(s[i]);
	}
//	stk.display();
	reverse(stk);
	return 0;
}
