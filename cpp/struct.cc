#include <iostream>
#include <cstring>

using namespace std;

struct Books 
{
	char title[60];
	char author[60];
	int year;
};

int main()
{
	struct Books Book1;
	struct Books Book2;

	strcpy(Book1.title, "Labreda"); 
	strcpy(Book1.author, "Hans Micah"); 
	Book1.year = 2013;
	
	strcpy(Book2.title, "Fault in our Suns"); 
	strcpy(Book2.author, "Johan Blue"); 
	Book2.year = 2002;

	cout<<Book1.title<<endl;
	cout<<Book1.author<<endl;
	cout<<Book1.year<<endl;
	cout<<endl;
	cout<<Book2.title<<endl;
	cout<<Book2.author<<endl;
	cout<<Book2.year<<endl;

	return 0;
}
