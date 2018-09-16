def zerofy(mat):
	try:
		rows = len(mat)
		cols = len(mat[0])
	except IndexError:
		return mat

	zeroth_row = False
	zeroth_col = False
	for i in range(rows):
		for j in range(cols):
			if mat[i][j]==0:
				if not i:
					zeroth_row=True
				if not j:
					zeroth_col=True
				if j>0 and i>0:
					mat[i][0]=0
					mat[0][j]=0

	for idx in range(cols):
		if mat[0][idx]==0:
			for idx2 in range(rows):
				mat[idx2][idx]=0

	for idx in range(rows):
		if mat[idx][0]==0:
			for idx2 in range(cols):
				mat[idx][idx2]=0
	if zeroth_col:
		for idx2 in range(rows):
				mat[idx2][0]=0
	if zeroth_row:
		for idx2 in range(cols):
				mat[0][idx2]=0

	print (mat)

def main():
	mat=[[1,1,1,1],[1,1,1,1],[0,1,1,0],[1,1,1,1]]
	zerofy(mat)

if __name__ == '__main__':
	main()