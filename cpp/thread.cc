#include <iostream>
#include <thread>
#include <chrono>

void first()
{

	int x, y, z;
	while (1)
		x = 2;
		y = 1;
		z = 13;
		x = x + y % z;
}


void second(int x)
{

	int y, z;
	while (1)
		y = 1;
		z = 17;
		x = x + y % z;
}

int main()
{
	std::thread hello (first);
	std::thread world (second, 7);

	std::cout<<"Running first and second thread... \n";

	std::this_thread::sleep_for(std::chrono::seconds(5));

	hello.join();
	world.join();

	std::cout<<"Completed first and second thread...\n";

	return 0;
}
