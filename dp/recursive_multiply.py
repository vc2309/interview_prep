def multiply(smaller,bigger):
	print(smaller,bigger)
	if smaller==0:
		return 0
	elif smaller==1:
		return bigger

	half = smaller>>1
	side1 = multiply(half,bigger)
	
	side2 = side1
	if smaller%2==1:
		print(side1,smaller,"odd")
		side2 = multiply(smaller-half,bigger)
	print side1,side2
	return side1+side2

# def main():
print multiply(3,11)