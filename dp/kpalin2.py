def edit2_distance(x,y):
	lx = len(x)
	ly = len(y)
	print(x,y)
	if not lx:
		return ly
	if not ly:
		return lx

	if x[-1]==y[-1]:
		return edit_distance(x[:lx-1],y[:ly-1])
	else:
		return min(1+edit_distance(x[:lx-2],y),1+edit_distance(x,y[:ly-2]))

def edit_distance(x,y):
	lx = len(x)
	ly = len(y)
	m=len(x)
	n=len(y)
	d={}
	print(x,y)
	for i in range(m+1):
		for j in range(n+1):
			if i==0 or j==0:
			    d[i,j]=0
			elif x[i-1]==y[j-1]:
			    d[i,j]=d[i-1,j-1]+1
			else:
			    d[i,j]=max(d[i-1,j],d[i,j-1])
	print(d)
	return d[m,n]

def is_k_palin(string,n):
	palin = string[::-1]
	count = edit_distance(string,palin)
	return int(len(string)-count<=n)

print(is_k_palin("abcbe",1))