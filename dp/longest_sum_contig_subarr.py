memo={}
def sum_cont(idx,arr):
	if idx==len(arr)-1:
		return arr[idx]

	if not memo.get(idx):
		memo[idx]=max(arr[idx],arr[idx]+sum_cont(idx+1,arr))

	return memo[idx]

def main():
	arr = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7] 
	(sum_cont(0,arr))
	print(max(memo.values()))

if __name__ == '__main__':
	main()