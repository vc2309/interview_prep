# Complete the primeQuery function below.
import math
class Tree(object):
    def __init__(self,n):
        self.Nodes = {(i+1):[] for i in range(n)}
        self.Vals = {(i+1):None for i in range(n)}
    def constructTree(self,first,second,values):
        for idx,x in enumerate(values):
            self.Vals[idx+1]=x
        for i in range(len(first)):
            node1 = first[i]
            node2 = second[i]
            self.Nodes[node1].append(node2)
            self.Nodes[node2].append(node1)
    def isPrime(self,num):
        if num==1:
            return 0
        for i in range(2,int(math.sqrt(abs(num)))+1):
            if num%i==0:
                return 0
        return 1
    def primeDFShelper(self,node,visited):
        if visited.get(node):
            return 0
        total = self.isPrime(self.Vals[node])
        visited[node]=True
        if self.Nodes.get(node):
            for child in self.Nodes.get(node):
                total+=self.primeDFShelper(child,visited)
        return total
    
    def regBFS(self,visited,start):
        queue = [1]
        done = False
        while len(queue) and not done:
            cur = queue.pop(0)
            if cur==start:
                for i in queue:
                    visited[i]=True
                done=True
                break
            visited[cur]=True
            for child in self.Nodes[cur]:
                if not visited.get(child):
                    queue.append(child)
        
    def primeDFS(self,start):
        visited = {}
        self.regBFS(visited,start)
        total = self.primeDFShelper(start,visited)
        return total

def primeQuery(n, first, second, values, queries):
    myTree = Tree(n)
    myTree.constructTree(first,second,values)
    return [ myTree.primeDFS(query) for query in queries]

