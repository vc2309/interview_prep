def steps(steps_left, steps_counts,hashmap):
	if steps_left==0:
		return 1
	elif steps_left>0:
		if hashmap.get(steps_left):
			return hashmap[steps_left]
		sum_steps=0
		for num_steps in steps_counts:
			sum_steps+=steps(steps_left-num_steps,steps_counts,hashmap)
		hashmap[steps_left]=sum_steps
		return sum_steps
	else:
		return 0

def main():
	steps_counts=[1,2,3]
	steps_left=int(input("eNTER num steps"))
	print (steps(steps_left,steps_counts,{}))

if __name__ == '__main__':
	main()