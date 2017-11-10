def main():
	a=[1,5,8,9,10,17,17,20]
	size=int(input("size\n"))
	rod(a,size)

def rod(a,size):
	dp={}
	i=size-1
	while i>0:
		dp[i]=max(rod_rec(a,i,dp)+rod_rec(a,i-1,dp),a[i-1])
		i-=1
	print(dp)

def rod_rec(a,size,dp):
	print(dp)
	if dp.get(size)==None:
		if size==1:
			dp[size]=a[size-1]
		else:
			dp[size]=rod_rec(a,size-1,dp)+rod_rec(a,1,dp)

	return dp[size]

if __name__ == '__main__':
	main()