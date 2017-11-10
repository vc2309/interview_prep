#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

bool is_balanced(string expression) {
    int l=expression.length();
    list<char> stack;
    map<char,char> pairs;
    pairs['}']='{';
    pairs[')']='(';
    pairs[']']='[';
    for(int i=0;i<l;i++){
        char c=expression[i];
        if(c=='{'||c=='('||c=='[')
        {
        stack.push_back(c);
        }
        else{
            if(pairs.count(c)==1){
                if (stack.back()==pairs[c]){
                    stack.pop_back();
                }
            }
        }
        
    }
    if(stack.size()>0){
        return false;
    }
    return true;
}

int main(){
    int t;
    cin >> t;
    ifstream inFile("q9.txt");
    ofstream outFile;
    outFile.open("result.txt");
    string expression;
    // inFile.('q9.txt');
    while(getline(inFile, expression)) {
        // cout<<expression<<endl;
        bool answer = is_balanced(expression);
        if(answer){
            cout << "YES\n";
            outFile<<("YES\n");}
        else {cout << "NO\n";
        outFile<<("NO\n");}}

    // for(int a0 = 0; a0 < t; a0++){
    //     string expression;
    //     cin >> expression;
    //     bool answer = is_balanced(expression);
    //     if(answer)
    //         cout << "YES\n";
    //     else cout << "NO\n";
    // }
    outFile.close();
    return 0;
}