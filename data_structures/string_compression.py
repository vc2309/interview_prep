def compress(a):
	ln = len(a)
	if not ln:
		return
	char = a[0]
	count = 1
	compressed = char
	for i in range(1,ln):
		if char!=a[i]:
			compressed+=str(count)
			count=1
			char=a[i]
			compressed+=char
		else:
			count+=1
	compressed+=str(count)

	return compressed

def main():
	word = input("Enter string \n")
	print(compress(word))

if __name__ == '__main__':
	main()