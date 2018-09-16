def get_max_sum(arr,idx,memo):
	if idx>=len(arr):
		return 0

	elif not memo.get(idx):
		highest_sum = 0
		for x in range(idx+2,len(arr)):
			highest_sum=max(highest_sum,get_max_sum(arr,x,memo))
		memo[idx]=arr[idx]+highest_sum

	return memo[idx]

def main():
	arr = [5,4,10,40,20,10,300]
	memo={}
	print(max(get_max_sum(arr,0,memo),get_max_sum(arr,1,memo)))

if __name__ == '__main__':
	main()