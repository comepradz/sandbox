#include <iostream>

using namespace std;

int i=0;

int main ()
{
	while (1) 
	{
		i += 1;
		cout<<i<<endl;
		if (i > 4096) break;
	}
return 0;
}
