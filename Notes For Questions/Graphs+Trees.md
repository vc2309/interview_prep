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