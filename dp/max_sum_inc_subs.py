memo={}
def msis(arr,n):
	if n==0:
		return arr[n]

	if not memo.get(n):
		try:
			memo[n]=max([msis(arr,i)+arr[n] for i in range(n) if arr[i]<arr[n]])
		except:
			memo[n]=arr[n]
	return memo[n]

def main():
	arr=[1, 11, 2, 3, 1, 4, 5,10,10,1,12,3]
	print(max([msis(arr,len(arr)-i) for i in range(1,len(arr))])) 

if __name__ == '__main__':
	main()