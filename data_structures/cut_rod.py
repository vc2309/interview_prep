def cut(n,memo):
	if n<=1:
		return 1
	if not memo.get(n):
		memo[n]=max([cut(n-i)*cut(i) for i in range(i,n)])
	return memo[n]

def main():
	n = int(input("enter len"))
	print(cut(n,{}))

if __name__ == '__main__':
	main()