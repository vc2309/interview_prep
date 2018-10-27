def max_prod_lis(arr):
	dp=[i for i in arr]
	for i in range(len(arr)-1,-1,-1):
		# print(i)
		max_prod = dp[i]
		for j in range(i,len(arr)):

			if arr[j]>arr[i]:
				print(arr[i],arr[j])
				max_prod=max(max_prod,dp[j]*dp[i])
		dp[i]=max_prod
	print(dp)
	return max(dp)

arr = [0,3, 100, 4, 5, 150, 6,11,0,3, 100, 4, 5, 150, 6,11,0,3, 100, 4, 5, 150, 6,11,0,3, 100, 4, 5, 150, 6,11,0,3, 100, 4, 5, 150, 6,11,0,3, 100, 4, 5, 150, 6,11,0,3, 100, 4, 5, 150, 6,11,0,3, 100, 4, 5, 150, 6,11,0,3, 100, 4, 5, 150, 6,11] 
print(max_prod_lis(arr))