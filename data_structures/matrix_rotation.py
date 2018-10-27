def rotate(mtr):
	layers = int(len(mtr)/2)
	size = len(mtr)-1
	for layer in range(layers):
		start = layer
		end = size - layer
		for i in range(start,end):
			offset = start-i
			tl = mtr[layer][i]
			tr = mtr[i][end]
			bl = mtr[end-i][layer]
			br = mtr[end][end-i]
			print(tl,tr,br,bl)
			mtr[layer][i] = bl
			mtr[i][end] = tl
			mtr[end-i][layer] = br
			mtr[end][end-i] = tr

	print_matrix (mtr)

def print_matrix(mtr):
	for row in mtr:
		for val in row:
			print(val)," ",
		print("")

mtr =[
[1,2,3,4],
[5,6,7,8,],
[9,10,11,12],
[13,14,15,16]

]

for i in range(4):
	rotate(mtr)
	print("")