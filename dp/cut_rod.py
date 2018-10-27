def cut(n,memo):
	if n<=1:
		return 1
	if not memo.get(n):
		memo[n]=max([max(cut(n-i,memo)*cut(i,memo),(n-i)*i) for i in range(1,n)])
	return memo[n]

def main():
	n = int(input("enter len"))
	print(cut(n,{}))

if __name__ == '__main__':
	main()