#include <iostream>
#include <string>
struct Node
{
	string val;
	Node *next;
	
};

struct LL
{
	Node *head;
	int len;
}

Node::Node(int val){
	(*this)->val=val;
}

int LL::get_len(){
	return this.len;
}

int main(int argc, char const *argv[])
{
	LL *my_ll = new LL;
	my_ll->head = new Node(5);
}