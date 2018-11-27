import numpy as np
class Graph(object):
	"""docstring for Graph"""
	def __init__(self, name):
		
		self.name=name
		self.graph={}

	def addNode(self,val):
		if self.graph.get(val)==None:
			self.graph[val]=[]
		else:
			print("Already exists")

	def addEdge(self,val1,val2):
		if self.graph.get(val1)!=None and self.graph.get(val2)!=None:
			if val2 in self.graph[val1]:
				print("edge already exists\n")
			else:
				self.graph[val1].append(val2)
				self.graph[val2].append(val1)

	def print(self):
		print("{}\n".format(self.name))
		for i in self.graph.keys():
			print("{} is connected to :- {}\n" .format(i,self.graph[i]))

	def BFS(self,s,g):
		queue=[]
		visited={v:False for v in self.graph.keys()}
		dist={v:None for v in self.graph.keys()}
		# post={v:None for v in self.graph.keys()}
		pre={v:None for v in self.graph.keys()}
		pre[s]="START"
		queue.append(s)
		dist[s]=0
		found=False
		while len(queue):
			cur=queue.pop(0)
			visited[cur]=True
			if cur==g:
				print("found")
				found=True
				break
			for child in self.graph[cur]:
				if not visited[child]:
					queue.append(child)
					if not dist.get(child):
						dist[child]=dist[cur]+1
						pre[child]=cur

		if cur!=g:
			print("No path")
		else:
			print(visited)
			print(dist)
			cur=g
			# print(pre)
			while cur!="START":
				print(cur,"<-")
				cur=pre[cur]

	def allPathsHelper(self,s,d,visited,path):
		print(s,d)
		visited[s]=True
		if s==d:
			visited[s]=False
			paths.append([d])
			return True
		found_path=False
		for i in self.graph[s]:
			if not visited.get(i):
				print("from",s,i)
				if self.allPathsHelper(i,d,visited,paths):
					paths[-1].append(s)
					found_path=True
		return found_path

		
	def allPaths(self,s,d):
		paths = []
		visited = {v:False for v in self.graph.keys()}
		self.allPathsHelper(s,d,visited,paths)
		print(paths)


			

def main():
	g=Graph(name="Friends")
	names=["Vishnu","Yash","Abeer","Vyoma","Namita","Shubhashish","Ameeq","Jaiman","Zubin","Siddhu","Bhavya","Manasi","Saisha","Malvika","Devki","Prannay","Maru","Ridhima"]
	for x in names:
		g.addNode(x)

	for i,x in enumerate(names):
		for j in range(3):
			ran=np.random.randint(0,len(names)-1)
			if ran!=i:
				g.addEdge(x,names[ran])

	g.print()
	s=input("Find path between?")
	f=input("and")
	g.allPaths(s,f)

if __name__ == '__main__':
	main()