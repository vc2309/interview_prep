def rod(n,lns,prices,memo):
	if n==0: return 0
	if not memo.get(n):
		memo[n] = max([rod(n-lns[i],lns,prices,memo)+prices[i] for i,j in enumerate(lns) if j<=n])
	return memo[n]

def main():
	
	prices= [1, 5, 8, 9, 10, 17, 17, 20]
	lns = [i for i in range(1,len(prices))]
	n = len(prices)

	print(rod(n,lns,prices,{}))

if __name__ == '__main__':
	main()