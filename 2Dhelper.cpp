#include<iostream>
#include<string>
using namespace std;
class Array {
	int arr[3][3] = { {1,2,3},{4,5,6},{7,8,9} };
public:
	Array()
	{

	}
	class Helper {
		int row;
		int col;
		Array *(*ptr);
	public :
	Helper(Array *(*ptr), int row , int col):ptr(ptr),row(row),col(col)
	{
	}
			operator int()
			{
				cout << "reading\n";
				return *(*(ptr+row)+col);
	        }
	};
};
