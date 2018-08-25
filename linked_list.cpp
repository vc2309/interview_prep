#include <iostream>
#include <string>
using namespace std;
struct Node
{
	string val;
	Node *next;
	
};

struct LL
{
	Node *head;
	Node *tail;
	int len;

LL(){
	this->head=NULL;
	this->len = 0;
	this->tail=NULL;
}

int get_len(){
	return this->len;
}

void push(string val){
	if (this->head==NULL){
		this->head=new Node;
		(this->head)->val=val;
		this->tail=this->head;
		this->len++;
	}
	else{
		Node *temp=new Node;
		temp->val=val;
		(*(this->tail)).next = temp;

		this->tail=temp;
		this->len++;
	}

}

void display(){
	Node *dummy=new Node;
	dummy=this->head;
	while(dummy->next!=NULL){
		cout<<dummy->val<<" ";
		dummy=dummy->next;
	}
}

string pop(){

	Node *dummy=this->head;
	if(dummy->next==NULL){
		return "underflow";
	}
	while((dummy->next)->next!=NULL)
	{
		dummy=dummy->next;
	}

	string val=(*(dummy->next)).val;
	delete dummy->next;
	return val;

}


};

int main(int argc, char const *argv[])
{
	LL *my_ll = new LL;
	my_ll->push("5");
	my_ll->push("6");
	my_ll->push("7");
	my_ll->push("8");
	my_ll->push("9");
	cout<<my_ll->pop();
	my_ll->display();

	cout<<"ok"<<endl;
	cout<<my_ll->get_len()<<endl;
}