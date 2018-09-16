def fibonnaci(n):
	fib = {0:0,1:1}
	for i in range(1,n+1):
		if not fib.get(i):
			fib[i]=fib[i-1]+fib[i-2]
	return fib[n]

def main():
	n=int(input("Enter number\n"))
	print(fibonnaci(n))

if __name__ == '__main__':
	main()