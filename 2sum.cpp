#include <iostream>
#include <map>
#include <vector>
using namespace std;
int main()
{
    map<int,int> a;
    vector<int> b;
    int n;
    cout<<"enter number of terms"<<endl;
    cin>>n;
    int target;
    cout<<"enter target"<<endl;
    cin>>target;
    while(n>0){
        int c;
        cin>>c;
        b.push_back(c);
        cout<<b[n];
        n--;
    }
    cout<<b.size()<<endl;
    cout<<"E"<<endl;
    vector<int>::iterator i;
    for(i=b.begin();i!=b.end();i++){
        a[(*i)]=(*i);  
    }
    map<int,int>::iterator j;
    for(j=a.begin();j!=a.end();j++){
        cout<<(*j).first<<endl;
    }
    for(int i=0;i<b.size();i++){
        if(a.count(target-b[i])==1){
            cout<<b[i]<<" "<<(target-b[i])<<endl;
        }
    }
}