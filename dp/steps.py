def steps(steps_left, steps_counts,hashmap):
	if steps_left==0:
		return 1
	elif steps_left<0:
		return 0
	if not hashmap.get(steps_left):
		hashmap[steps_left]=0
		for i in steps_counts:
			if i<=steps_left:
				hashmap[steps_left]+=steps(steps_left-i,steps_counts,hashmap)
	return hashmap[steps_left]

def main():
	steps_counts=[1,2,3]
	steps_left=int(input("eNTER num steps"))
	print (steps(steps_left,steps_counts,{}))

if __name__ == '__main__':
	main()