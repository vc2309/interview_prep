#ifndef _QUEUE_H_
#define _QUEUE_H_
#include <stddef.h>
template <typename T>
class Queue
{
private:
	template <typename U>
	class Node
	{
	public:

		U val;
		Node<U> *next;
		Node(U val){
			this->val=val;
			this->next=nullptr;
		};
		~Node();
		
	};

	int len;
	Node<T>* front;
	Node<T>* end;

public:

	T pop();
	void push(T val);
	void display();
	Queue();
	~Queue();
	
};
#endif