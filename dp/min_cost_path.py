def min_cost(matrix,dp,i,j):
	if i<0 or j<0:
		return float('inf')
	if i==j==0:
		return matrix[0][0]

	elif not dp.get((i,j)):
		dp[(i,j)] = matrix[i][j] + min(min_cost(matrix,dp,i-1,j),min_cost(matrix,dp,i,j-1),min_cost(matrix,dp,i-1,j-1))
	return dp[(i,j)]

matrix = ([

[1,2,3],
[4,8,2],
[1,5,3]

	])

n=len(matrix)-1
m=len(matrix[0])-1

print(min_cost(matrix,{},n,m))