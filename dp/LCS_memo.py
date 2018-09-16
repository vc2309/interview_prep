def lcs(a,b,cache):
	la = len(a)-1
	lb = len(b)-1
	if la==-1 or lb==-1:
		return 0

	# print(la,lb)
	# print(len(cache),len(cache[0]))
	if cache[lb][la]==None:

		diff = int(a[la]==b[lb])
		cache[lb][la]=  max(diff+ lcs(a[:la],b[:lb],cache),
									lcs(a,b[:lb],cache),
									lcs(a[:la],b,cache)
									)

	return cache[lb][la]

def main():
	a=input("Enter a\n")
	b=input("Enter b\n")
	cache = [[None for i in range(len(a))] for j in range(len(b))]

	# print(cache)
	print(lcs(a,b,cache))

if __name__ == '__main__':
	main()