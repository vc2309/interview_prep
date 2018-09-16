memo={}
def msis(arr,n):
	if n==0:
		return 1

	if not memo.get(n):
		try:
			memo[n]=max([msis(arr,i)+1 for i in range(n) if arr[i]<arr[n]])
		except:
			memo[n]=1
	return memo[n]

def main():
	arr=[10, 22, 9, 33, 21, 50, 41, 60, 80]
	print(max([msis(arr,len(arr)-i) for i in range(1,len(arr))])) 

if __name__ == '__main__':
	main()