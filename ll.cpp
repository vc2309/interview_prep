#include <iostream>
#include <cstdlib>
using namespace std;

struct node{
    int val;
    node* next;
};

void push(node*  &t,int &c);
void pop(node * &h,int &c);
void display(node* h,int c);

int main(){
    node* h;
    node* t;
    int count=0;
    // t.next=NULL;
    h=NULL;
    int choice;
    choice=-99;
    while(choice!=0){

        cout<<"1 push 2 pop 3 display"<<endl;
        cin>>choice;
        if(choice==1){
            // if(count==0){
                push(t,count);
                if(h==NULL){
                    h=t;
                }
                // count++;
            // }
            cout<<h->val<<endl;
            // cout<<t.val<<endl;
        }
        else if(choice==2){
            pop(h,count);
        }
        else if(choice==3){
            // cout<<h->val<<endl;
            display(h,count);
        }
        else{exit(0);};
    }
return 0;
}

void push(node*& t,int &c){
    node* n;
    n=new node;
    cout<<"enter val"<<endl;
    int a;
    cin>>a;
    n->val=a;
    n->next=NULL;

    if(t==NULL){
        // t->next=n;
        t=n;
    }
    else{
        t->next=n;
        t=n;
    }
    
    c++;
    
}

void pop(node* &h,int &c){
    if(c==0){
        cout<<"underflow!"<<endl;
    }
    else{
        h=h->next;
        c--;
    }
}

void display(node* h,int c){
    // cout<<h->val<<endl;
    while(c>0){
        cout<<h->val<<" ";
        // h=*(h.next);
        h=h->next;
        c--;
    }
    cout<<""<<endl;
}