def main():
	a=[-2,-3,4,-1,-4,1,5,-33]
	dp=[[None for x in range(len(a)-1)] for i in range(len(a)-1)]
	# max_sum=get_max(a,dp)
	print(maxSubArraySum(a,len(a)))

def get_max(a,dp):
	for i in range(len(a)-1):
		if i>0:
			dp[0][i]=dp[0][i-1]+a[i]
		else:
			dp[0][i]=a[i]

	for i in range(1,len(a)):
		for j in range(i,len(a)-1):
			if dp[i][j]==None:
				dp[i][j]=dp[i-1][j]-dp[0][j-1]

	print(dp)
	m=dp[0][0]
	for i in dp:
		for j in i:
			if j:
				if m<j:
					m=j
	print(m)
def maxSubArraySum(a,size):
     
    max_so_far =a[0]
    curr_max = a[0]
     
    for i in range(1,size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far,curr_max)
         
    return max_so_far
if __name__ == '__main__':
	main()

