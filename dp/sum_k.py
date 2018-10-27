def sum_k(arr,k):
	n=len(arr)
	dp=[[0 for i in range(n+1)] for j in range(k+1)]

	for kth in range(1,k+1):
		for i in range(1,n+1):
			num=arr[i-1]
			# set max number of subsequences to subs using all numbers prior to this one
			dp[kth][i] = dp[kth][i-1]

			#if the current number is less than k, then we explore other possibilities

			if num<=kth:
				dp[kth][i]+=1 + dp[kth-num][i-1]
	for row in dp:
		print (row)
	return dp[k][n]

print(sum_k([1,2,3,4],10))
