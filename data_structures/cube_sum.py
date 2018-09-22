def cube_sum(n):
	mem = {}
	for a in range(n):
		for b in range(n):
			ans = a**3 * b**3
			if not mem.get(ans):
				mem[ans]=[]
			mem[ans].append((a,b))
	for ans in mem.keys():
		arr = mem[ans]
		for i in arr:
			for j in arr:
				print i,j

cube_sum(1000)
