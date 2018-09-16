def knapsack(W, weights, values):
	K={w:v for w,v in zip(weights,values)}
	for i in range(W+1):
		max_weight=0
		for j,wi in enumerate(weights):
			if wi <=i:
				rem_val=K.get(i-wi) if K.get(i-wi) else 0
				max_weight=max(rem_val+wi,rem_val)
		K[i]=max_weight
	return K[W]

def main():
	weights=[2,2,3,4]
	values=[10,40,30,100]
	print("Weight\tValue")
	for w,v in zip(weights,values):
		print(str(w)+"\t"+str(v))
	W=int(input("Enter weight"))
	print(knapsack(W,weights,values))

if __name__ == '__main__':
	main()