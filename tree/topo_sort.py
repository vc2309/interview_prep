class Graph(object):
    def __init__(self):
        self.graph = {}
    def add_vertex(self,name):
        if not self.graph.get(name):
            self.graph[name]=[]
    def add_edge(self,edge):
        try:
            self.graph[edge[0]].append(edge[1])
        except Exception as e:
            print(e)
    def print_graph(self):
        for V in self.graph.items():
            print(V[0],end=" : ")
            for vert in V[1]:
                print(vert,end=" ")
            print("")

def previsit(v,pre,clock,visited):
    visited[v]=True
    clock=clock+1
    pre[v]=clock
    return clock
def postvisit(v,post,clock,visited):
    clock=clock+1
    post[v]=clock
    return clock

def topo_sort_helper(G,v,visited,pre,post,clock):
    clock=previsit(v,pre,clock,visited)
    print("clock after",v,clock)
    for u in G.graph.get(v):
        if not visited.get(u):
            clock=topo_sort_helper(G,u,visited,pre,post,clock)
    clock=postvisit(v,post,clock,visited)
    return clock
    
def topo_sort(G):
    pre={}
    post={}
    visited={}
    clock=0
    for vertex in G.graph.keys():
        if not visited.get(vertex):
            clock=topo_sort_helper(G,vertex,visited,pre,post,clock)
    order = [(i[0],i[1]) for i in post.items() ]
    order = sorted(order,key= lambda x:x[1],reverse=True)
    print(order)
G= Graph()
# import unichar
verts = [chr(i) for i in range(65,72)]
for i in verts:
    G.add_vertex(i)
edges = [ ("A","B"), ("B","D"), ("B","C"), ("C","E"), ("C","F"), ("F","D"), ("C","D"), ("D","E")]
for edge in edges:
    G.add_edge(edge)
G.print_graph()
topo_sort(G)