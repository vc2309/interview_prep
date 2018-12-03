# Graphs and Trees

## Traversals

### DFS
- Idea : For each node `u`, add each *unvisited* child `u` to the stack. While the stack is not empty, we keep popping the top of the stack and applying the same method.

1. Recursive method
	```python
	def DFS(v,visited,graph):
		visited[v]=True
		for u in graph[v]:
			if not visited[u]:
				DFS(u,visited,graph)
	```
2. Iterative method
	```python
	def DFS(graph):
		visited = {}
		for v in graph.keys():
			if visited.get(v):
				continue
			stack = []
			stack.push(v)
			while len(stack):
				curr = stack.pop()
				visited
				for u in graph.get(curr):
					if not visited.get(u):
						stack.append(u)
	```

#### Printing all paths
	```python
	def helper(G,s,d,visited,path):
		path.append(s)
		if s==d:
			print(path)
		else:
			visited[s]=True
			for u in G.graph[s]:
				if not visited.get(u):
					helper(G,u,d,visited,path)
		visited[s]=False
		path.pop()
	```
- Explanation: 
1. We add the current node to the path
2. If the current node is destination, we print path
3. Else, we mark current node as visited and carry out recursive calls for each child. We mark the parent (current) as visited so that we do not encounter any cycles back to this parent node while we are within its recursive interval.
4. At the end of the for loop, we have effecitvely exited the dfs interval of the node s. This means we can take it off the stack and the path. We mark it as not visited so that another call to this function will still be able to explore a new path which utilizes this node.

#### Applications
1. Detecting cycles
2. Path finding
- Can give a destination node and return the path when reached.
- 