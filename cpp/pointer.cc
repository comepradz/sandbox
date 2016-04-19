#include <iostream>

using std::cout;
using std::endl;

int x;
int *y;

int main()
{
	y = &x;
	x = 5;

	cout<<x<<endl;
	cout<<*y<<endl;
	cout<<y<<endl;
	cout<<&x<<endl;

	*y = 500;

	cout<<x<<endl;
	cout<<*y<<endl;
	cout<<y<<endl;
	cout<<&x<<endl;

	return 0;
}
