def rope_cut(ln,memo):
	
	if ln==1:
		return 1

	if not memo.get(ln):
		memo[ln]=max([max(rope_cut(ln-li,memo),ln-li)*li for li in range(1,ln)])10
	return memo[ln]

def main():
	n = int(input("enter n\n"))
	print(rope_cut(n,{}))

if __name__ == '__main__':
	main()
