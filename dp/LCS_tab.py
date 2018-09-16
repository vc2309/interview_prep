def lcs(a,b,cache):
	for x in range(len(a)+1):
		for y in range(len(b)+1):
			if x==0 or y==0:
				cache[x][y]=0
			elif a[x-1]==b[y-1]:
				cache[x][y]=1+cache[x-1][y-1]
			else:
				cache[x][y]=max(cache[x-1][y],cache[x][y-1])
	return cache[-1][-1]

def main():
	a=input("Enter a\n")
	b=input("Enter b\n")
	cache = [[None for i in range(len(b)+1)] for j in range(len(a)+1)]

	# print(cache)
	print(lcs(a,b,cache))

if __name__ == '__main__':
	main()