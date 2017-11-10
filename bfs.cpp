#include<iostream>
#include <list>
#include<vector>
#include<unordered_map>
 
using namespace std;

class Graph{
    int V;
    list<int> *adj;
public:
    Graph(int V);
    void addEdge(int v,int w);
    void BFS(int s);
    void print_all();
    void DFS(int s);
    void DFSUtil(int s, bool visited);
};
void Graph::print_all(){
    int itr=0;
    list<int>::iterator itr2;
    int i=0;
    for(itr=0;itr!=V;itr++){
        for(itr2=adj[itr].begin();itr2!=adj[itr].end();itr2++){
            cout<<(itr)<<"-->"<<(*itr2)<<endl;
        }
        i++;
    }
}
Graph::Graph(int V){
    this->V=V;
    adj=new list<int>[V];
}

void Graph::addEdge(int v, int w){
    adj[v].push_back(w);
}

void Graph::BFS(int s){
    unordered_map<int,bool> visited;
    list<int>queue;
    queue.push_back(s);
    list<int>::iterator i;
    while(queue.size()>0){
        int current=queue.front();
        cout<<" "<<current<<endl;
        queue.pop_front();
        visited[current]=true; //cout<<""<<endl;
        for(i=adj[current].begin();i!=adj[current].end();i++){
           
            // cout<<(*i)<<endl;
            if(visited.count((*i))<1){
                // cout<<(*i)<<" ";
                visited[(*i)]=true;
                queue.push_back(*i);
            }
        }
    }

}

void Graph::DFSUtil(int v, bool visited[])
{
    // Mark the current node as visited and
    // print it
    visited[v] = true;
    cout << v << " ";
 
    // Recur for all the vertices adjacent
    // to this vertex
    list<int>::iterator i;
    for (i = adj[v].begin(); i != adj[v].end(); ++i)
        if (!visited[*i])
            DFSUtil(*i, visited);
}
 
// DFS traversal of the vertices reachable from v.
// It uses recursive DFSUtil()
void Graph::DFS(int v)
{
    // Mark all the vertices as not visited
    bool *visited = new bool[V];
    for (int i = 0; i < V; i++)
        visited[i] = false;
 
    // Call the recursive helper function
    // to print DFS traversal
    DFSUtil(v, visited);
}

int main()
{
    // Create a graph given in the above diagram
    Graph g(5);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(2, 3);
    g.addEdge(2, 4);
    g.addEdge(3, 4);
    g.addEdge(4, 5);
    g.addEdge(5,1);
 
    g.print_all();
    cout << "Following is Breadth First Traversal "
         << "(starting from vertex 2) \n";
    g.BFS(2);
 
    return 0;
}