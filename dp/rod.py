def rod(length,L,V,memo):
	if length==0:
		return 0

	if not memo.get(length):
		memo[length]=max([rod(length-li,L,V,memo)+V[i] for i,li in enumerate(L) if li<=length])
	return memo[length]

def main():
	L=[1  , 2  , 3  , 4  , 5  , 6   ,7   ,8 ]
	V=[ 3  , 5  , 8 ,  9  ,10  ,17 , 17,  20]
	print(rod(4,L,V,{}))
	

if __name__ == '__main__':
	main()