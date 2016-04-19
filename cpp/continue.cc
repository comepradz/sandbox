#include <iostream>

using namespace std;

int i=0;
enum BOOLEAN {FALSE, TRUE};

int main()
{
	BOOLEAN HAHA(TRUE);
	while (1) 
	{
		i += 1;
		cout<<i<<endl;
		if (i < 4096) continue;
	}
return 0;
}
