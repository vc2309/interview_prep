#include "queue.h"
#include <iostream>
#include <string>
using namespace std;

int main(int argc, char const *argv[])
{
	Queue<string> *my_queue = new Queue<string>();
	for (int i = 1; i < argc; ++i)
		{
			my_queue->push(argv[i]);
		}	
		my_queue->display();
	return 0;
}