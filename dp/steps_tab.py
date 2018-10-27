
def steps(steps_left,steps_counts):
	num_steps = {(i):0 for i in range(steps_left+1)}
	num_steps[0]=1
	num_steps[1]=1
	for j in range(2,steps_left+1):
		for i in steps_counts:
			if i<=j:
				num_steps[j]+=num_steps[j-i]
	return num_steps[steps_left]

def main():
	steps_counts=[1,2,3]
	steps_left=int(input("eNTER num steps"))
	print (steps(steps_left,steps_counts))

if __name__ == '__main__':
	main()