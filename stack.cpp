#include <iostream>
#include <string>
using namespace std;

template <typename T>
class Stack
{
private:
	template <typename U>
	class Node
	{
	public:
			Node<U> *next;
			U val; 
			Node(U val){
				this->val=val;
			}
		~Node();
		
	};

Node<T> *top;
int len;

public:

	void push(T val){
		Node<T> * dummy = new Node<T>(val);
		dummy->next = this->top;
		this->top = dummy;
		this->len++;
	}

	int get_len(){
		return this->len;
	}

	T pop(){
		if (this->len<=0) {
			cout<<"Underflow";
			return NULL; 
		}
		T dummy = (this->top)->val;
		this->top= (this->top)->next;
		this->len--;
		return dummy;

	}

	void display(){
		Node<T> *dummy;
		dummy = this->top;
		while(dummy!=NULL){
			cout<<dummy->val<<endl;
			dummy=dummy->next;
		}
		cout<<""<<endl;
	}

	Stack(){
		this->top=NULL;
		this->len=0;
	}
	~Stack();
	
};

int main(){

	Stack<int> *myStack = new Stack<int>();
	myStack->push(5);
	myStack->push(6);
	myStack->push(7);
	myStack->push(8);
	myStack->display();
	myStack->pop();
	myStack->display();
	cout<<myStack->get_len();
	return 1;
}
