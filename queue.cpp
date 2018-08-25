#include "queue.h"
#include <iostream>
#include <string>
using namespace std;
template <typename T>
Queue<T>::Queue()
{
	this->front = nullptr;
	this->end=nullptr;
	this->len = 0;
}

template <typename T>
void Queue<T>::push(T val)
{
	Node<T> *dummy = new Node<T>(val);
	if(this->len==0){
		this->front=dummy;
		this->end=dummy;
	}
	else{
		(this->end)->next = dummy;
		this->end=dummy;
	}
	this->len++;
}

template <typename T>
T Queue<T>::pop(){
	if(this->len==0){
		cout<<"Underflow"<<endl;
		return NULL;
	}

	T val = (this->front)->val;
	this->front=(this->front)->next;
	this->len--;
	return val;
}

template <typename T>
void Queue<T>::display(){
	Node<T> *dummy=this->front;
	while(dummy!=NULL){
		cout<<dummy->val<<" ";
		dummy=dummy->next;
	}
	cout<<"\n";
}

int main(int argc, char const *argv[])
{
	Queue<string> *my_queue = new Queue<string>();
	for (int i = 1; i < argc; ++i)
		{
			my_queue->push(argv[i]);
		}	
		my_queue->display();
		my_queue->pop();
		my_queue->display();
		my_queue->pop();
		my_queue->display();
		my_queue->pop();
		my_queue->display();
		my_queue->pop();
		my_queue->display();

	return 0;
}
