
class Graph(object):
	"""docstring for Tree"""
	def __init__(self):
		self.nodes = []
		self.outgoing = {}
		self.incoming = {}

	def addNode(self,name):
		self.nodes.append(name)

	def initEdges(self):
		for node in self.nodes:
			self.outgoing[node]={i:False for i in self.nodes}
			self.incoming[node]={i:False for i in self.nodes}

	def addEdge(self,edge):
		self.outgoing[edge[0]][edge[1]]=True
		self.incoming[edge[1]][edge[0]]=True

	def deleteEdge(self,edge):
		self.outgoing[edge[0]][edge[1]]=False
		self.incoming[edge[1]][edge[0]]=False

	def nextJob(self,order):
		while self.nodes:
			n = self.nodes.pop(0)
			if not sum(self.incoming.get(n).values()):
				for u in self.outgoing.get(n):
					self.deleteEdge((n,u))
				order.append(n)
			else:
				self.nodes.append(n)
		return order

	def buildOrder(self,nodes,edges):
		for node in nodes:
			self.addNode(node)
		self.initEdges()
		# print(self.nodes)
		for edge in edges:
			self.addEdge(edge)
		# print(self.edges)
		print(self.nextJob([]))

def main():
	g = Graph()
	for i in range(10000):
		g.buildOrder(
		["a","b","c","d","e","f","g","h","i","j","k","l"],
	[("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c"),("i","j"),("l","i"),("a","l"),("i","k"),("b","i")]
	)

if __name__ == '__main__':
	main()