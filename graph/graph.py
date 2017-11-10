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
		visited=[]
		queue.append(s)
		while(len(queue)>0):
			cur=queue.pop(0)
			visited.append(cur)
			if cur==g:
				print("found")
				break
			for child in self.graph[cur]:
				if child not in visited and child not in queue:
					queue.append(child)
		if cur!=g:
			print("No path")
		else:
			print(visited)


			

def main():
	g=Graph(name="Friends")
	names=["Vishnu","Yash","Abeer","Vyoma","Namita","Shubhashish","Ameeq","Jaiman","Zubin","Siddhu","Bhavya","Manasi","Saisha","Malvika","Devki"]
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
	g.BFS(s,f)

if __name__ == '__main__':
	main()