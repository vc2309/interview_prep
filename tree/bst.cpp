#include <iostream>
#include <string>
#include <stdlib.h>
#include <cmath>
using namespace std;

class Node
{
	
public:
	int val;
	Node *left;
	Node *right;
	Node *parent;
	Node(int val){
		this->val=val;
		this->left=NULL;
		this->right=NULL;
		this->parent=NULL;

	};
	Node(){
		// this->val=NULL;
		this->left=NULL;
		this->right=NULL;
		this->parent=NULL;
	};

	~Node();
	
};

class BST
{
	

public:
	Node *root;
	BST(){
	this->root = NULL;
	};
	~BST();

	void insert(int val)
	{
		if((this->root)==NULL){
			this->root=new Node(val);
		}
		else
		{
			Node *cur = this->root;
			Node *att = this->root;
			while((cur!=NULL))
			{
				att=cur;
				if (cur->val>val)
				{
					cur=cur->left;
				}
				else{
					cur=cur->right;
				}
			}
			cur=new Node(val);
			cur->parent=att;
			if (val>att->val)
			{
				att->right=cur;
			}
			else{
				att->left=cur;
			}
		}
	}

	void preorder(Node *root)
	{
		if(root==NULL)
		{
			cout<<"\n";
		}
		else
		{
			cout<<root->val;
			preorder(root->left);
			preorder(root->right);
		}

	}

	void inorder(Node *root)
	{
		if (root==NULL)
		{
			cout<<"";
		}

		else if ((root->left==NULL)&&(root->right==NULL))
		{
			cout<<root->val<<endl;
		}
		else{
			inorder(root->left);
			cout<<root->val<<endl;
			inorder(root->right);
		}
	}

	int get_height(Node *root)
	{
		if (root==NULL)
		{
			return 0;
		}
		else
		{
			return max((1+this->get_height(root->left)),(1+this->get_height(root->right)));
		}
	}

	bool check_balanced(Node *root)
	{
		if (root==NULL)
		{
			return true;
		}
		cout<<root->val<<"node"<<abs(this->get_height(root->left)-this->get_height(root->right))<<endl;
			cout<<(this->get_height(root->left))<<this->get_height(root->right)<<endl;
		if ((this->get_height(root->left)==this->get_height(root->right)) || abs(this->get_height(root->left)-this->get_height(root->right))==1)
		{
			
			return this->check_balanced(root->left)&&this->check_balanced(root->right);
		}
		return false;
	}

	Node* search(int val)
	{
		Node* cur = this->root;
		Node* trkr = this->root;
		while(cur!=NULL)
		{
			trkr=cur;
			if (cur->val>val)
			{
				cur=cur->left;
			}
			else if(val>cur->val)
			{
				cur=cur->right;
			}
			else
			{
				return trkr;
			}
		}
		return cur;
	}

	int minimum(Node *ref)
	{
		while(ref->left!=NULL)
		{
			ref=ref->left;
		}
		return ref->val;
	}

	int successor(int val)
	{
		Node *trkr = this->search(val);
		int suc = -1;
		if (trkr!=NULL)
		{
			if (trkr->right!=NULL)
			{
				suc = this->minimum(trkr->right);
			}
			else
			{
				Node* y=trkr->parent;
				while(y->right==trkr && trkr!=NULL)
				{
					trkr=y;
					y=y->parent;
				}
				suc=y->val;
			}
		}
		return suc;
	}
	
};

int main(int argc, char const *argv[])
{
	BST *my_bst = new BST();
	for (int i = 1; i < argc; ++i)
	{
		my_bst->insert(atoi(argv[i]));
	}

	my_bst->preorder(my_bst->root);
	my_bst->inorder(my_bst->root);
	cout<<my_bst->check_balanced(my_bst->root)<<endl;
	cout<<my_bst->successor(5);
	cout<<my_bst->successor(4);
}