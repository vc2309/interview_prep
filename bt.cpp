#include <iostream>
using namespace std;

struct node{
    int val;
    node *l;
    node *r;
};
void push(node* &root,int v);
void in_order(node* root);
void post_order(node* root);
int main(){
    node* root;
    root=new node;
    root=NULL;

    int choice=-99;
    while(choice!=0){
        cout<<'\n';
        cout<<"1 push 2 pop 3 inorder 4 postorder"<<endl;
        cin>>choice;
        switch(choice){
            case 1: {cout<<"enter val"<<endl;
                    int v;
                    cin>>v;
                    push(root,v);
            }
            break;
            case 3: {
                in_order(root);
                cout<<""<<endl;
            }
            break;
            case 4:{
                post_order(root);
            }
            break;
            default:exit(0);
        }
    }
    return 0;
}

void push(node* &root,int v){
    if(root==NULL){
        node *n;
        n=new node;
        n->val=v;
        n->l=NULL;
        n->r=NULL;
        root=n;
    }
    else{
        if(root->val>v){
            push(root->l,v);
        }
        else if(root->val<v){
            push(root->r,v);
        }
        else{
            cout<<"same val"<<endl;
        }
    }
}

void in_order(node* root){
    if(root->l==NULL && root->r==NULL){
        cout<<root->val<<" ";
    }
    else if(root->l==NULL && root->r!=NULL){
        cout<<root->val<<" ";
        in_order(root->r);
    }
    else if(root->r==NULL && root->l!=NULL){
        in_order(root->l);
        cout<<root->val<<" ";
    }
    else{
        in_order(root->l);
        cout<<root->val<<" ";
        in_order(root->r);
    }
}

void post_order(node* root){
    if(root->l==NULL && root->r==NULL){
        cout<<root->val<<" ";
    }
    

    else if(root->r==NULL && root->l!=NULL){
        post_order(root->l);
        cout<<root->val<<" ";
    }
    else if(root->l==NULL && root->r!=NULL){
        post_order(root->r);
        cout<<root->val<<" ";
    }
    else{
        post_order(root->l);
        post_order(root->r);
        cout<<root->val<<" ";
    }
}