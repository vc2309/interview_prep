def ugly(n):
	tot = 1
	ug = {1:True}
	nos = [1]
	facs = [5,3,2]
	ctr=1
	while(tot<=n):
		for x in facs:
			if ctr%x==0 and ug.get(ctr/x):
				ug[ctr]=True
				nos.append(ctr)
				tot+=1
				break
		ctr+=1

	return nos[n-1]

def main():
	# n = int(input("Enter n\n"))
	print("\n",ugly(150))

if __name__ == '__main__':
	main()
