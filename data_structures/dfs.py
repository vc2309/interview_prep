# Python program to print DFS traversal from a
# given given graph
from collections import defaultdict

# This class represents a directed graph using
# adjacency list representation
class Graph(object):

	# Constructor
	def __init__(self):

		# default dictionary to store graph
		self.graph = defaultdict(list)
		self.clock=0

	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)
		if not self.graph.get(v):
			self.graph[v]=[]

	# A function used by DFS
	def DFSUtil(self,v,visited,pre,post):
		pre[v]=self.clock
		self.clock+=1
		
		visited[v]= True
		print v,
		for i in self.graph[v]:
			if visited[i] == False:
				self.DFSUtil(i,visited,pre,post)
		post[v]=self.clock
		self.clock+=1


	# The function to do DFS traversal. It uses
	# recursive DFSUtil()
	def DFS(self,v):
		pre = {}
		post = {}
		clock=0
		# Mark all the vertices as not visited
		visited = [False]*(len(self.graph))

		# Call the recursive helper function to print
		# DFS traversal
		self.DFSUtil(v,visited,pre,post)
		print(pre,post)

	def cycleHelper(self,v,visited,recStack):
		recStack[v]=True
		visited[v]=True
		# print(v,recStack)
		for u in self.graph[v]:
			# print v,u,recStack[u]
			if not visited[u]:
				if self.cycleHelper(u,visited,recStack):
					return True
			elif recStack[u]:
				return True

		recStack[v]=False
		return False

	def getCycle(self):
		visited = {v:False for v in self.graph.keys()}
		recStack = {v:False for v in self.graph.keys()}

		for v in self.graph.keys():
			if not visited[v]:
				if self.cycleHelper(v,visited,recStack):
					return True
		return False


	def BFS(self):
		pre = {}
		post = {}
		visited = {v:False for v in self.graph.keys()}
		q=[]
		clock = 0
		num_trees = 0
		for v in self.graph.keys():
			
			if not visited[v]:
				print("tree number",num_trees,"starting at node",v)
				num_trees+=1
				q = [v]
				while len(q):
					curr = q.pop(0)
					visited[curr]=True
					pre[curr]=clock
					clock+=1
					for u in self.graph[curr]:
						if not visited[u]:
							q.append(u)
					# post[curr]=clock
					# clock+=1
		print(pre)

# Driver code
# Create a graph given in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(4, 5)
g.addEdge(1, 3)
g.addEdge(3, 1)
print g.graph
print "Following is DFS from (starting from vertex 2)"
g.BFS()
print(g.getCycle())
# print(pre,post)
# This code is contributed by Neelam Yadav
