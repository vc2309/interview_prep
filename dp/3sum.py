def sum3(nums,n,memo):
	if n==0:
		return 1
	
	if not memo.get(n):
		memo[n]=0
		for num in nums:
			if num<=n:
				memo[n]+=sum3(nums,n-num,memo)

	return memo[n]

def main():
	nums=[1,3,5]
	memo={}
	n=int(input("enter n\n"))
	print(sum3(nums,n,memo))

if __name__ == '__main__':
	main()