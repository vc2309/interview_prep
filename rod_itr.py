def main():
	a=[1,5,8,9,10,17,17,20]
	size=int(input("size\n"))
	rod(a,size)

def rod(a,size):
	dp=[0 for x in range(size+1)]

	for i in range(1,size+1):
		max_val=-9999
		for j in range(i):
			max_val=max(max_val,a[j]+dp[i-j-1])
		dp[i]=max_val

	print(dp)

if __name__ == '__main__':
	main()