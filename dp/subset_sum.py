def subset_sum(arr,k,pos):
	if pos==0 and k!=0:
		return False
	if k==0:
		return True

	if (arr[pos - 1] > k): 
		return subset_sum(arr, k,pos-1)

	return subset_sum(arr,k-arr[pos-1],pos-1) or subset_sum(arr,k,pos-1)


def isSubsetSum(set,n, sum) : 
	dp=[[False for i in range(n+1)] for j in range(sum+1) ]
	dp[0] = [True]*n
	for i in range(1,sum+1):
		for j in range(1,n+1):
			num=arr[j-1]
			dp[i][j]=dp[i][j-1]
			if num<=i:
				dp[i][j]=(dp[i][j]) or (dp[i-num][j-1] or dp[i][j-1])

	return dp[sum][n]
    

arr = [3, 34, 12, 5, 2]
k = 200
n = len(arr)
print(subset_sum(arr,k,n))
print(isSubsetSum(arr,n,k))